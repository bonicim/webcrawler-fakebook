import sys
import urllib.request
import urllib.parse
import re
import http.cookiejar
import src.my_htmlparser

FAKEBOOK_LOGIN_URL = 'http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/'
FAKEBOOK_DOMAIN_URL = 'http://cs5700sp15.ccs.neu.edu'
NEXT_VAL = '/fakebook/'


def open_friend_page(friend_url):
    """Opens fakebook friend page given a 'friend_url'.
    Returns a String html landing page of the friend's fakebook profile."""
    pass


def open_view_friends_page(friend_page_url):
    """Opens the view friends link on a fakebook member page"
    Returns a String html page showing the list of friends of a given fakebook member."""
    pass


def parse_flags_friends_nextpage(fb_lpage_html, parser):
    """Parses a fakebook member's landing page for secret flags, friends, and a next page link
    Returns a dictionary consisting of the following key value pairs:
    'flag': [str_flag]
    'friend': [friend_rel_url]
     'next_page': [next_page_url]"""
    # TODO
    dict_ret = {}
    dict_ret['flag'] = parse_flag(fb_lpage_html, parser)
    dict_ret['friend'] = parse_friend(fb_lpage_html, parser)
    dict_ret['next_page'] = parse_next_page(fb_lpage_html, parser)
    return dict_ret

# Helpers


def parse_flag(fb_lpage_html, parser):
    parser.feed(fb_lpage_html)
    return list(filter(lambda x: 'FLAG' in x, parser.data_actual))


def parse_friend(fb_lpage_html, parser):
    return []


def parse_next_page(fb_lpage_html, parser):
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


def init_cookiejar():
    cj = http.cookiejar.CookieJar()
    return urllib.request.HTTPCookieProcessor(cj)


def build_custom_opener(cookiejar):
    return urllib.request.build_opener(cookiejar)


def init_html_parser():
    parser = src.my_htmlparser.MyHTMLParser()
    parser.links = {}  # we are adding an attribute to the HTMLParser class
    parser.data_actual = []
    return parser


def get_csrf_token_fakebook(opener, parser):
    resp_login_page = opener.open(FAKEBOOK_LOGIN_URL)
    html_login = resp_login_page.read().decode()
    return parse_token(html_login, parser)


def parse_token(html_page, parser):
    """Gets csrf token from a Fakebook login page"""
    parser.feed(html_page)
    links = parser.links
    csrf_dict = parser.links['csrf']
    for key in csrf_dict:
        if key == 'value':
            return csrf_dict[key]
    print("FAILURE. We should have parsed csrf token.")


def login_fakebook(csrf_token, opener, username, password, url=FAKEBOOK_LOGIN_URL):
    """Logs into http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/ with 'username' and 'password'
    Returns a String html landing page of the user's account."""
    values = {'username': username, 'password': password, 'next': NEXT_VAL, 'csrfmiddlewaretoken': csrf_token}
    data = urllib.parse.urlencode(values).encode()
    return opener.open(url, data).read().decode()


def main():
    # Accumulators
    # list_frontier = []
    # list_flags = []
    # set_users = set()

    # Setup opener to access internet
    opts = getopts(sys.argv)
    cookiejar = init_cookiejar()
    opener = build_custom_opener(cookiejar)

    # Setup parser to parse html pages
    parser = init_html_parser() # Really bad design choice, implementation coupled with this parser

    # Get csrf token
    csrf_token = get_csrf_token_fakebook(opener, parser)

    # Login to Fakebook, parse for targets
    # links of friends, search for flags, and the next friends or link to list of friends
    html_login = login_fakebook(csrf_token, opener, opts[0], opts[1])
    print(html_login)
    dict_tgts = parse_flags_friends_nextpage(html_login, parser)
    for key in dict_tgts:
        print("Key: ", key, " Value: ", dict_tgts[key])

    # Access a Friends page and scrape

    # Finish scraping the site and print the results


if __name__ == "__main":
    main()


main()
