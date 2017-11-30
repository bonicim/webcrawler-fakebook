import socket
import urllib.request
import urllib.parse
import html.parser
import http.cookies
import http.cookiejar
import time
import htmlparser
import threading
import sys


def getopts(argv):
    # TODO
    pass


def login_fakebook(username, password):
    """Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username' and 'password'
    Returns a String html landing page of the user's account."""
    pass


def open_friend_page(friend_url):
    """Opens fakebook friend page given a 'friend_url'.
    Returns a String html landing page of the friend's fakebook profile."""
    pass


def open_view_friends_page(friend_page_url):
    """Opens the view friends link on a fakebook member page"
    Returns a String html page showing the list of friends of a given fakebook member."""
    pass


def parse_flags_friends_nextpage(fb_lpage_html):
    """Parses a fakebook member's landing page for secret flags, friends, and a next page link
    Returns a dictionary consisting of the following key value pairs:
    'flag': [str_flag]
    'friends': [friend_rel_url]
     'next_page': [next_page_url]"""
    pass

# Helpers


def add_secret_flag(new_flag, collection_flag):
    """Adds new_flag to collection_flag. Returns the updated list."""
    pass


def add_friend(friend, collection_friend):
    """Returns updated collection_friend"""
    pass


def is_unique_user(friend, collection_friend):
    """Returns true if friend is not in collection_friend; false otherwise."""
    pass


def add_friend_to_frontier(friend, collection_frontier):
    """Returns updated collection_frontier"""
    pass


def remove_friend_to_frontier(collection_frontier):
    """Removes a random friend from collection_frontier
     and returns a Tuple consisting of the removed friend and updated collection."""
    pass


def create_get_req(url):
    """Returns a GET Request object given a String url."""
    pass


def create_post_req(url, data):
    """Returns a POST Request object given a String url and Bytes data."""
    pass


def create_fb_absolute_url(friend_rel_url):
    """Returns an absolute url based on Fakebook domain and relative domain of a Fakebook member.
    The relative url must be in the form: /fakebook/<uniqueID>/
    The Fakebook domain used is http://cs5700sp15.ccs.neu.edu/

    For example, given relative url /fakebook/50644342/, the absolute url will be:
    http://cs5700sp15.ccs.neu.edu/fakebook/50644342/"""
    pass


def main():
    lock = threading.Lock
    list_frontier = []
    list_flags = []
    set_users = set()
    my_args = getopts(sys.argv)


def is_5(x):
    return x == 5


if __name__ == "__main":
    main()


main()
