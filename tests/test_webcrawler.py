import unittest
import pytest
import src.webcrawler
import tests.util_test
import urllib.request
import tests.util_test_html
import src.my_htmlparser


SECRET_FLAG_LEN = 64

class WebcrawlerTestCase(unittest.TestCase):
    """ Tests for webcrawler.py.
    All functions beginning with test will be run when unittest.main() is called. """
    def test_getopts_returns_username_password(self):
        """Is a list containing username and password retrieved?"""
        assert src.webcrawler.getopts(tests.util_test.ARGV) == ['bonicillo.m', 'toast']

    def test_getopts_returns_error(self):
        """Does error get returned if 0, 1, or 3 more arguments are given?"""
        with self.assertRaises(SystemExit):
            src.webcrawler.getopts(['toast'])

    def test_login_fakebook_success(self):
        """Does a valid user's fakebook profile get returned?"""
        pytest.skip()

    def test_login_fakebook_failure(self):
        """Does an error page for an invalid fakebook profile get returned?"""
        pytest.skip()

    def test_open_friend_page_success(self):
        """Does a valid fakebook landing page of a friend get returned?"""
        pytest.skip()

    def test_open_friend_page_failure(self):
        """Does an error page for an invalid fakebook profile get returned?"""
        pytest.skip()

    def test_open_view_friends_page_success(self):
        """Does a fakebook view friends page of a valid friend get returned?"""
        pytest.skip()

    def test_open_view_friends_page_failure(self):
        """Does an error page for an invalid view friends url get returned?"""
        pytest.skip()

    def test_parse_csrf_success(self):
        """Does a """

    def test_parse_flag_where_flag_present(self):
        """Does a list of one flag get returned?"""
        html = tests.util_test_html.FAKEBOOK_LOGIN_YES_FLAG_HTML
        flag_tuple = src.webcrawler.parse_flag(html, tests.util_test.init_parser())
        self.assertIsNotNone(flag_tuple)
        for flag in flag_tuple:
            assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN

    def test_parse_flag_where_multi_flag_present(self):
        """Does a list of three flags get returned?"""
        html = tests.util_test_html.FAKEBOOK_LOGIN_YES_3_FLAG_HTML
        flag_tuple = src.webcrawler.parse_flag(html, tests.util_test.init_parser())
        self.assertIsNotNone(flag_tuple)
        assert len(flag_tuple) == 3
        for flag in flag_tuple:
            assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN
        html = tests.util_test_html.FAKEBOOK_LOGIN_YES_4_FLAG_HTML
        flag_tuple = src.webcrawler.parse_flag(html, tests.util_test.init_parser())
        self.assertIsNotNone(flag_tuple)
        assert len(flag_tuple) == 4
        for flag in flag_tuple:
            assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN

    def test_parse_flag_where_flag_absent(self):
        """Does an empty list get returned?"""
        flag_tuple = \
            src.webcrawler.parse_flag(tests.util_test_html.FAKEBOOK_LOGIN_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(flag_tuple)
        assert len(flag_tuple) == 0

    def test_parse_friend_where_friends_present(self):
        """Does a list of friend url's get returned?"""
        tup_friend_url = \
            src.webcrawler.parse_friend(tests.util_test_html.MEMBER_LANDING_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_friend_url)
        assert len(tup_friend_url) == 10
        assert '/fakebook/190909169/' in tup_friend_url
        tup_friend_url = \
            src.webcrawler.parse_friend(tests.util_test_html.FRIEND_VIEWING_FRIENDS_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_friend_url)
        assert len(tup_friend_url) > 0
        assert '/fakebook/89081356/' in tup_friend_url

    def test_parse_friend_where_no_friends_except_user(self):
        """Does an empty list get returned?"""
        tup_friend_url = \
            src.webcrawler.parse_friend(tests.util_test_html.FRIEND_LANDING_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_friend_url)
        assert len(tup_friend_url) == 1
        tup_friend_url = \
            src.webcrawler.parse_friend(tests.util_test_html.FAKEBOOK_LOGIN_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_friend_url)
        assert len(tup_friend_url) == 0

    def test_parse_next_page_where_next_exists(self):
        """Does a dictionary containing 3 key value pairs in which the next_page key has
        an empty list get returned?"""
        # Case 1: Friend viewing friends page
        tup_next_page = \
            src.webcrawler.parse_next_page(tests.util_test_html.FRIEND_VIEWING_FRIENDS_HTML,
                                           tests.util_test.init_parser())
        self.assertIsNotNone(tup_next_page)
        assert len(tup_next_page) > len('/fakebook/996350946/')
        assert tup_next_page[0] == '/fakebook/996350946/friends/2/'

        # Case 2: Landing page of friend where the next page must be the first page
        tup_next_page = \
            src.webcrawler.parse_next_page(tests.util_test_html.FRIEND_LANDING_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_next_page)
        assert len(tup_next_page) > len('/fakebook/996350946/')
        assert tup_next_page[0] == '/fakebook/996350946/friends/1/'

    def test_parse_next_page_where_next_absent(self):
        """Does a dictionary containing 3 key value pairs get returned?"""
        # Case 1: My Landing page has no next links because I have few friends
        tup_next_page = \
            src.webcrawler.parse_next_page(tests.util_test_html.MEMBER_LANDING_HTML, tests.util_test.init_parser())
        self.assertIsNotNone(tup_next_page)
        assert len(tup_next_page) == 0

        # Case 2: The last page of a friend's list of friends. There is no next.
        tup_next_page = \
            src.webcrawler.parse_next_page(tests.util_test_html.FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML,
                                           tests.util_test.init_parser())
        self.assertIsNotNone(tup_next_page)
        assert len(tup_next_page) == 0

    def test_create_get_req_friend_url_success(self):
        """Is a GET Request object created given a valid url?"""
        self.assertIsInstance(src.webcrawler.create_get_req(tests.util_test.FRIEND_HOME_URL),
                              urllib.request.Request)

    def test_create_post_req_fb_login_success(self):
        """Is a POST Request object created given a valid url?"""
        self.assertIsInstance(src.webcrawler.create_post_req(tests.util_test.FRIEND_HOME_URL, tests.util_test.LOGIN_DATA),
                              urllib.request.Request)

    def test_create_fb_absolute_url_success(self):
        """Is an absolute FB url created given a relative friend url?"""
        assert src.webcrawler.create_fb_absolute_url('/fakebook/50644342/') == \
               tests.util_test.FB_URL_PREFIX + '/fakebook/50644342/'


if __name__ == '__main__':
    unittest.main()
