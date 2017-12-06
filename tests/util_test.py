import urllib.parse
import src.my_htmlparser
import http.cookiejar
import urllib.request

USERNAME = 'bonicillo.m'
PASSWORD = 'toast'
REL_FRIEND_URL = '/fakebook/50644342'
FRIEND_HOME_URL = 'http://cs5700sp15.ccs.neu.edu/fakebook/50644342/'
FRIEND_VIEW_FRIENDS_URL = 'http://cs5700sp15.ccs.neu.edu/fakebook/50644342/friends/1/'
ARGV = ['webcrawler', USERNAME, PASSWORD]
FB_URL_PREFIX = 'http://cs5700sp15.ccs.neu.edu'
FB_LOGIN_URL = 'http://cs5700sp15.ccs.neu.edu/accounts/login/?next=/fakebook/'
LOGIN_DATA = urllib.parse.urlencode(
    {'username': USERNAME,
     'password': PASSWORD,
     'next': '/fakebook/',
     'csrfmiddlewaretoken': 'foobar'})


def init_parser():
    parser = src.my_htmlparser.MyHTMLParser()
    return parser


def init_opener():
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

