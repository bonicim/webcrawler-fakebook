import sys
import urllib.request
import urllib.parse
import http.cookiejar
import src.my_htmlparser
import queue
from threading import Thread
import time


# global vars
FAKEBOOK_LOGIN_URL = 'http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/'
FAKEBOOK_DOMAIN_URL = 'http://cs5700sp15.ccs.neu.edu'
NEXT_VAL = '/fakebook/'
VALUES_USERNAME = 'username'
VALUES_PASSWORD = 'password'
VALUES_NEXT = 'next'
VALUES_CSRF = 'csrfmiddlewaretoken'
NUM_THREADS = 10

friend_frontier_q = queue.Queue()  # thread safe
flags_q = queue.Queue()
visited_set = frozenset()  # thread safe


def open_friend_page(friend_url, opener):
    """Opens fakebook friend page given a 'friend_url'.
    Returns a dictionary of relevant info from a fakebook page"""
    try:
        pass
    except:
        pass
    return dict()

def parse_flags_friends_pagelist(fb_lpage_html, parser):
    """Parses a fakebook member's landing page for secret flags, friends, and a next page link
    Returns a dictionary consisting of the following key value pairs:
    'flag': (str_flag,)
    'friend': (friend_rel_url,)
     'next_page': (next_page_url,)"""
    dict_ret = {}
    parser.feed(fb_lpage_html)
    dict_ret['flags'] = parser.secret_flags()
    dict_ret['friends'] = parser.friends()
    dict_ret['page_list'] = parser.pagelist()
    return dict_ret


def parse_flag(fb_lpage_html, parser):
    parser.feed(fb_lpage_html)  # assumes that html is a raw string; might be a problem when getting html from site
    return parser.secret_flags()


def parse_friend(fb_lpage_html, parser):
    parser.feed(fb_lpage_html)
    return parser.friends()


def parse_next_page(fb_lpage_html, parser):
    parser.feed(fb_lpage_html)
    return parser.pagelist()


def add_friend(friend, collection_friend):
    """Returns updated collection_friend"""
    pass


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
        resp_login_page = opener.open(url)
        html_login = resp_login_page.read().decode()
        parser.feed(html_login)
        data = parser.csrf_token()[0]
    except urllib.request.URLError:
        data = 'URL not found.'
    return data

def login_fakebook(csrf_token, opener, username, password, url=FAKEBOOK_LOGIN_URL):
    """Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username' and 'password'
    Returns a String html landing page of the user's account."""
    values = {VALUES_USERNAME: username, VALUES_PASSWORD: password, VALUES_NEXT: NEXT_VAL, VALUES_CSRF: csrf_token}
    try:
        data = urllib.parse.urlencode(values).encode()
        data = opener.open(url, data).read().decode()
    except urllib.request.URLError:
        data = 'URL not found.'
    return data

def main():
    # Accumulators
    # list_frontier = []
    # list_flags = []
    # set_users = set()

    # Setup opener to access internet; parser
    opts = getopts(sys.argv)
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    parser = src.my_htmlparser.MyHTMLParser()

    # Login to Fakebook, parse for targets
    csrf_token = get_csrf_token(opener, parser)
    html_login = login_fakebook(csrf_token, opener, opts[0], opts[1])
    dict_ret = parse_flags_friends_pagelist(html_login, parser)
    if len(dict_ret['flags']) > 0:
        for flag in dict_ret['flags']:
            flags_q.put(flag)
    if len(dict_ret['friends']) > 0:
        for flag in dict_ret['flags']:
            friend_frontier_q.put(flag)
    # Note: assumes member does not have more than one page of friends

    # create threads; each thread has its own parser and opener
    # kickoff threads to search each friend

    # Finish scraping the site and print the results
    print('Main complete.')

if __name__ == "__main":
    main()


main()
