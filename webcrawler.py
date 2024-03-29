#!/usr/bin/env python3.6
import sys
import urllib.request
import urllib.parse
import http.cookiejar
import src.my_htmlparser
import threading
import time
import queue
from config.webcrawler_config import FAKEBOOK_LOGIN_URL, FAKEBOOK_DOMAIN_URL, NEXT_VAL, \
	VALUES_USERNAME, VALUES_PASSWORD, VALUES_NEXT, VALUES_CSRF, NUM_THREADS

q_frontier = queue.Queue()  # thread safe
q_flags = []  # thread safe manually
visited_set = frozenset()  # thread safe manually
total_loop_count = 0
total_URL_not_found = 0


def main():
	# Setup admin
	start_time = time.time()
	lock = threading.Lock()
	threads = []
	opts = getopts(sys.argv)

	# Setup Opener and Parser
	cj = http.cookiejar.CookieJar()
	opener = create_custom_opener(cj)
	parser = src.my_htmlparser.MyHTMLParser()

	# Login to Fakebook and initialize queue with friends
	csrf_token = get_csrf_token(opener, parser)
	html_login = login_fakebook(csrf_token, opener, opts[0], opts[1])
	dict_tgt = parse_flags_friends_page_list(html_login, parser)
	add_flags_to_flag_queue(dict_tgt['flags'], lock)
	add_friends_to_frontier(dict_tgt['friends'])
	# ASSUMPTION: member does not have more than 20 friends and thus no page 2 of friends

	# Kickoff and end web scraping
	setup_threads(threads, cj, lock)
	stop_threads(threads)

	scraper_output(start_time)


def parse_flags_friends_page_list(html_fakebook, parser):
	"""Parses a fakebook member's landing page for secret flags, friends, and a next page link
    Returns a dictionary consisting of the following key value pairs:
    'flag': (str_flag,)
    'friend': (friend_rel_url,)
     'next_page': (next_page_url,)"""
	dict_ret = {}
	parser.feed(html_fakebook)
	dict_ret['flags'] = parser.secret_flags_attr()  # a tuple
	dict_ret['friends'] = parser.friends()  # a tuple
	dict_ret['page_list'] = parser.pagelist()  # a tuple
	return dict_ret


def create_get_req(url):
	#TODO: keep-alive make one connection to be more efficient
	"""Returns a GET Request object given a String url."""
	return urllib.request.Request(url)


def create_post_req(url, data):
	"""Returns a POST Request object given a String url and Bytes data.
    Does not validate arguments."""
	return urllib.request.Request(url, data)


def create_fb_absolute_url(friend_rel_url):
	"""Returns an absolute url based on Fakebook domain and relative domain of a Fakebook member.
	The relative url MUST be in the form: /fakebook/<uniqueID>/
	(where uniqueID is the unique ID of a Fakebook user) For example, given relative url
	/fakebook/50644342/, the absolute url will be: http://cs5700sp15.ccs.neu.edu/fakebook/50644342/"""
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
	global total_URL_not_found
	try:
		html_login = opener.open(url).read().decode()
		parser.feed(html_login)
		data = parser.csrf_token()[0]
	except urllib.request.URLError:
		total_URL_not_found += 1
		data = 'URL not found: ' + url
	return data


def login_fakebook(csrf_token, opener, username, password, url=FAKEBOOK_LOGIN_URL):
	"""Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username'
	and 'password' Returns a String html landing page of the user's account."""
	global total_URL_not_found
	values = {VALUES_USERNAME: username, VALUES_PASSWORD: password, VALUES_NEXT: NEXT_VAL, VALUES_CSRF: csrf_token}
	try:
		data_sent = urllib.parse.urlencode(values).encode()
		data_received = opener.open(url, data_sent).read().decode()
		return data_received
	except urllib.request.HTTPError as e:
		total_URL_not_found += 1
		code = e.code
		if code == 500:
			print('HTTP error code: ', code, ' Need to call login again')
			login_fakebook(csrf_token,opener, username, password)
		elif code == 403 or e.code == 404:
			print("Abandoning search.")


def get_all_friends_flags(url, opener):
	global total_URL_not_found
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
	except urllib.request.HTTPError as e:
		total_URL_not_found += 1
		code = e.code
		if code == 500:
			# print('HTTP error code: ', code, " Ping URL again.")
			return get_all_friends_flags(url, opener)
		elif code == 403 or e.code == 404:
			print("Abandoning search.")


def get_all_friends_flags_helper(opener, friend_list, flag_list, page_list_set, visited_page_set,
								 parser):
	"""Opens fakebook friend page given a 'friend_url'. Returns a tuple of list of fakebook
	friends of the fakebook user"""
	global total_URL_not_found
	url = None
	for page in page_list_set:
		if page not in visited_page_set:
			url = page
			break
	# Base case
	if url is None:
		return friend_list, flag_list
	try:
		resp = opener.open(create_fb_absolute_url(url))
		page_list_set.remove(url)
		visited_page_set.add(url)
		html_friends = resp.read().decode()
		dict_ret = parse_flags_friends_page_list(html_friends, parser)
		friend_list.extend(list(dict_ret['friends']))
		flag_list.extend(list(dict_ret['flags']))
		for el in dict_ret['page_list']:
			page_list_set.add(el)
	except urllib.request.HTTPError as e:
		total_URL_not_found += 1
		code = e.code
		if code == 403 or code == 404:  # abandon search
			print("Abandoning search of URL.")
			page_list_set.remove(url)
			visited_page_set.add(url)
		elif code == 500:
			pass
			# print('HTTP error code: ', code, " Ping URL again.")
		elif code == 301:
			print("Should not see this. Python handles redirects automatically")
	finally:
		return get_all_friends_flags_helper(opener, friend_list, flag_list, page_list_set,
											visited_page_set, parser)


def process_url(url, cj, lock):
	global visited_set
	global total_loop_count
	global q_flags
	with lock:
		visited_set = visited_set.union((url,))
	opener = create_custom_opener(cj)
	friends_list, flags_list = get_all_friends_flags(create_fb_absolute_url(url), opener)
	friends_list_no_dupes = list(filter(lambda x: x not in visited_set, friends_list))
	potential_loop_count = len(friends_list) - len(friends_list_no_dupes)
	with lock:
		q_flags = q_flags + flags_list
		total_loop_count += potential_loop_count
	for friend in friends_list_no_dupes:
		q_frontier.put(friend)


def worker(cj, lock):
	print(threading.current_thread().getName(), 'Starting')
	while True:
		try:
			url = q_frontier.get()
			if url is None:
				break
			if url not in visited_set:
				process_url(url, cj, lock)
		except queue.Empty as e:
			print("We should not see this because Queue will block until an item is found.")
			print(e)
		finally:
			q_frontier.task_done()


def create_custom_opener(cj):
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	opener.addheaders.append(("Connection", "keep-alive"))
	return opener


def add_flags_to_flag_queue(flags_iter, lock):
	global q_flags
	with lock:
		q_flags = q_flags + list(flags_iter)


def add_friends_to_frontier(friends_iter):
	for friend in friends_iter:
		q_frontier.put(friend)


def setup_threads(threads, cj, lock):
	for i in range(NUM_THREADS):
		t = threading.Thread(target=worker, args=(cj, lock), name='Worker ' + str(i))
		threads.append(t)
		t.start()
	scraper_feedback()
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
	print("Workers count: ", NUM_THREADS)
	# print("Total URL Not Found: ", total_URL_not_found)
	# print("Remaining queue should be zero: ", q_frontier.qsize())
	# print("Potential loop count: ", total_loop_count)
	print("Flags count: ", len(q_flags))
	print("Printing flags if any found: ")
	if len(q_flags) != 0:
		for flag in q_flags:
			print(flag)
	else:
		print("No flags found.", '\n')
	print("Friend Count: ", len(visited_set))


def scraper_feedback():
	print("Scraping Fakebook: ", FAKEBOOK_DOMAIN_URL)
	print('Workers tasked: ', NUM_THREADS)
	print('Depending on the machines computing power, this might take awhile (avg 3-10 min).......')


if __name__ == "__main":
	main()

main()
