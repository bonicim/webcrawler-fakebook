import sys
import urllib.request
import urllib.parse
import http.cookiejar
import src.my_htmlparser
import threading
import time

import src.webcrawler_config
from src.webcrawler_config import FAKEBOOK_LOGIN_URL, FAKEBOOK_DOMAIN_URL, NEXT_VAL, \
	VALUES_USERNAME, VALUES_PASSWORD, VALUES_NEXT, VALUES_CSRF, NUM_THREADS, q_frontier, \
	visited_set, total_loop_count


def parse_flags_friends_page_list(html_fakebook, parser):
	"""Parses a fakebook member's landing page for secret flags, friends, and a next page link
    Returns a dictionary consisting of the following key value pairs:
    'flag': (str_flag,)
    'friend': (friend_rel_url,)
     'next_page': (next_page_url,)"""
	dict_ret = {}
	parser.feed(html_fakebook)
	dict_ret['flags'] = parser.secret_flags()  # a tuple
	dict_ret['friends'] = parser.friends()  # a tuple
	dict_ret['page_list'] = parser.pagelist()  # a tuple
	return dict_ret


def create_get_req(url):
	"""Returns a GET Request object given a String url."""
	return urllib.request.Request(url)


def create_post_req(url, data):
	"""Returns a POST Request object given a String url and Bytes data.
    Does not validate arguments."""
	return urllib.request.Request(url, data)


def create_fb_absolute_url(friend_rel_url):
	"""Returns an absolute url based on Fakebook domain and relative domain of a Fakebook member.
    The relative url MUST be in the form: /fakebook/<uniqueID>/
    (where uniqueID is the unique ID of a Fakebook user)
    The Fakebook domain used is http://cs5700sp15.ccs.neu.edu/

    For example, given relative url /fakebook/50644342/, the absolute url will be:
    http://cs5700sp15.ccs.neu.edu/fakebook/50644342/"""
	return FAKEBOOK_DOMAIN_URL + friend_rel_url


def getopts(argv):
	"""Returns a list of 2 strings--username and password--in that order."""
	opts = []  # Empty dictionary to store key-value pairs.
	if len(argv) == 3:
		for arg in argv[1:]:
			opts.append(arg)
	else:
		print("Only enter exactly 2 arguments: username and password. Retry.")
		sys.exit()
	return opts


def get_csrf_token(opener, parser, url=FAKEBOOK_LOGIN_URL):
	try:
		html_login = opener.open(url).read().decode()
		parser.feed(html_login)
		data = parser.csrf_token()[0]
	except urllib.request.URLError:
		data = 'URL not found: ' + url
	return data


def login_fakebook(csrf_token, opener, username, password, url=FAKEBOOK_LOGIN_URL):
	"""Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username' and 'password'
    Returns a String html landing page of the user's account."""
	values = {VALUES_USERNAME: username, VALUES_PASSWORD: password,
			  VALUES_NEXT: NEXT_VAL, VALUES_CSRF: csrf_token}
	try:
		data_sent = urllib.parse.urlencode(values).encode()
		data_received = opener.open(url, data_sent).read().decode()
	except urllib.request.URLError:
		data_received = 'URL not found: ' + url
	return data_received


def get_all_friends_flags(url, opener):
	parser = src.my_htmlparser.MyHTMLParser()
	try:
		dict_ret = parse_flags_friends_page_list(opener.open(url).read().decode(), parser)
		friend_list = []
		flag_list = []
		page_list_set = set()
		friend_list.extend(list(dict_ret['friends']))
		flag_list.extend(list(dict_ret['flags']))
		for page in dict_ret['page_list']:
			page_list_set.add(page)
		return get_all_friends_flags_helper(opener, friend_list, flag_list, page_list_set, set(),
											parser)
	except urllib.request.URLError:
		print('URL not found: ', url)
		return [], []


def get_all_friends_flags_helper(opener, friend_list, flag_list, page_list_set, visited_page_set,
								 parser):
	"""Opens fakebook friend page given a 'friend_url'.
    Returns a tuple of list of fakebook friends of the fakebook user"""
	url = None
	for page in page_list_set:
		if page not in visited_page_set:
			url = page
			page_list_set.remove(page)
			visited_page_set.add(page)
			break
	if url is None:
		return friend_list, flag_list
	try:
		html_friends = opener.open(create_fb_absolute_url(url)).read().decode()
		dict_ret = parse_flags_friends_page_list(html_friends, parser)
		friend_list.extend(list(dict_ret['friends']))
		flag_list.extend(list(dict_ret['flags']))
		for el in dict_ret['page_list']:
			page_list_set.add(el)
	except urllib.request.URLError:
		print('URL not found: ', url)
	finally:
		return get_all_friends_flags_helper(opener, friend_list, flag_list, page_list_set,
											visited_page_set, parser)


def process_url(url, opener, lock):
	with lock:
		src.webcrawler_config.visited_set = src.webcrawler_config.visited_set.union((url,))
	friends_list, flags_list = get_all_friends_flags(create_fb_absolute_url(url), opener)
	friends_list_no_dupes = list(filter(lambda x: x not in visited_set, friends_list))
	potential_loop_count = len(friends_list) - len(friends_list_no_dupes)
	with lock:
		src.webcrawler_config.total_loop_count += potential_loop_count
	for friend in friends_list_no_dupes:
		src.webcrawler_config.q_frontier.put(friend)
	with lock:
		src.webcrawler_config.q_flags = src.webcrawler_config.q_flags + flags_list


def worker(opener, lock):
	print(threading.current_thread().getName(), 'Starting')
	while True:
		try:
			url = q_frontier.get()
			if url is None:
				break
			if url not in visited_set:
				print("Visiting Friend: ", url)
				process_url(url, opener, lock)
				print("Finished visiting Friend ", url)
		except:
			print("Getting an item in frontier failed.")
		finally:
			q_frontier.task_done()
	print("Frontier count: ", q_frontier.qsize())
	print("Friend count: ", len(visited_set), '\n')
	print(threading.current_thread().getName(), 'Exiting', '\n')


def create_custom_opener():
	return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(
		http.cookiejar.CookieJar()))


def add_flags_to_flag_queue(flags_iter, lock):
	with lock:
		src.webcrawler_config.q_flags = src.webcrawler_config.q_flags + list(flags_iter)


def add_friends_to_frontier(friends_iter):
	for friend in friends_iter:
		q_frontier.put(friend)


def setup_threads(threads, opener, lock):
	for i in range(NUM_THREADS):
		t = threading.Thread(target=worker, args=(opener, lock), name='Worker ' + str(i))
		threads.append(t)
		t.start()
	q_frontier.join()


def stop_threads(threads):
	for i in range(NUM_THREADS):
		q_frontier.put(None)
	for t in threads:
		t.join()


def scraper_output(start_time):
	end_time = time.time()
	print()
	print("Start time: ", start_time)
	print("End time: ", end_time)
	duration = (end_time - start_time)
	hours = duration // 3600
	minutes = duration // 60 - hours * 60
	print("Time to complete: ", hours, ' hours and ', minutes, ' minutes.')
	print("Remaining queue should be zero: ", q_frontier.qsize())
	print("Potential loop count: ", total_loop_count)
	print("Flags count: ", len(src.webcrawler_config.q_flags))
	print("Friend count should be about 2500: ", len(visited_set))


def main():
	# Setup admin
	start_time = time.time()
	lock = threading.Lock()
	threads = []
	opts = getopts(sys.argv)

	# Setup Opener and Parser
	opener = create_custom_opener()
	parser = src.my_htmlparser.MyHTMLParser()

	# Login to Fakebook and initialize queue with friends
	csrf_token = get_csrf_token(opener, parser)
	html_login = login_fakebook(csrf_token, opener, opts[0], opts[1])
	dict_tgt = parse_flags_friends_page_list(html_login, parser)
	add_flags_to_flag_queue(dict_tgt['flags'], lock)
	add_friends_to_frontier(dict_tgt['friends'])
	# ASSUMPTION: member does not have more than

	# Kickoff and end web scraping
	setup_threads(threads, opener, lock)
	stop_threads(threads)

	scraper_output(start_time)


if __name__ == "__main":
	main()

main()
