import sys
import urllib.request
import urllib.parse
import re
import http.cookiejar
import src.my_htmlparser

FAKEBOOK_LOGIN_URL = 'http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/'
FAKEBOOK_DOMAIN_URL = 'http://cs5700sp15.ccs.neu.edu'
NEXT_VAL = '/fakebook/'


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


def login_fakebook(csrf_token, opener, username, password, url=FAKEBOOK_LOGIN_URL):
    """Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username' and 'password'
    Returns a String html landing page of the user's account."""
    values = {'username': username, 'password': password, 'next': NEXT_VAL, 'csrfmiddlewaretoken': csrf_token}
    data = urllib.parse.urlencode(values)
    data = data.encode()
    resp = opener.open(url, data)
    resp = resp.read().decode()
    return resp


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
    'friend': [friend_rel_url]
     'next_page': [next_page_url]"""
    dict_ret = {}
    dict_ret['flag'] = parse_flag(fb_lpage_html)
    dict_ret['friend'] = parse_friend(fb_lpage_html)
    dict_ret['next_page'] = parse_next_page(fb_lpage_html)
    return dict_ret

# Helpers


def parse_flag(fb_lpage_html):
    return []


def parse_friend(fb_lpage_html):
    return []


def parse_next_page(fb_lpage_html):
    return re.findall(r'<ul id="pagelist">(.*?)</ul', fb_lpage_html)


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


def parse_token(html_page, parser):
    """Gets csrf token from a Fakebook login page"""
    # this is where you use HTML parser
    parser.feed(html_page)
    links = parser.links
    csrf_dict = parser.links['csrf']
    for key in csrf_dict:
        if key == 'value':
            return csrf_dict[key]
    print("FAILURE. We should have parsed csrf token.")


def init_html_parser():
    parser = src.my_htmlparser.MyHTMLParser()
    parser.links = {} # we are adding an attribute to the HTMLParser class
    return parser


def main():
    # Login to the Fakebook
    opts = getopts(sys.argv)
    cj = http.cookiejar.CookieJar()
    cjhandler = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cjhandler)
    resp = opener.open(FAKEBOOK_LOGIN_URL)

    html_page = resp.read().decode()

    # setup parser
    parser = init_html_parser()
    csrf_token = parse_token(html_page, parser)
    # member_page_html = login_fakebook(csrf_token, opener, opts[0], opts[1])
    # print(member_page_html)

    # Access a Friends page and scrape
    # list_frontier = []
    # list_flags = []
    # set_users = set()

    # Finish scraping the site and print the results


if __name__ == "__main":
    main()


main()
