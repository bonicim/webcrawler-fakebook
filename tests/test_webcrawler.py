import unittest
import pytest
import src.webcrawler
import tests.test_const
import urllib.request


class WebcrawlerTestCase(unittest.TestCase):
    """ Tests for webcrawler.py.
    All functions beginning with test will be run when unittest.main() is called. """

    def test_getopts_returns_username_password(self):
        """Is a list containing username and password retrieved?"""
        assert src.webcrawler.getopts(tests.test_const.ARGV) == ['bonicillo.m', 'toast']

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

    def test_parse_flags_friends_my_fb_page(self):
        """Does a dictionary containing 3 key value pairs in which the next_page key has
        an empty list get returned?"""
        dict_ret = src.webcrawler.parse_flags_friends_nextpage(tests.test_const.MEMBER_LP_HTML)
        assert len(dict_ret['next_page']) == 0
        assert len(dict_ret['friend']) == 10
        assert len(dict_ret['flag']) == 0

    def test_parse_flags_friends_nextpage_friend(self):
        """Does a dictionary containing 3 key value pairs get returned?"""
        dict_ret = src.webcrawler.parse_flags_friends_nextpage(tests.test_const.FRIEND_LP_HTML)
        for list_el in dict_ret:
            assert len(list_el) == 0

    def test_parse_flags_friends_viewing_friends_html(self):
        """Does a dictionary containing 3 key value pairs in which the flags key has
        an empty list get returned?"""
        dict_ret = src.webcrawler.parse_flags_friends_nextpage(tests.test_const.VIEWING_FRIENDS_HTML)
        assert len(dict_ret['flag']) == 0
        assert len(dict_ret['friend']) == 20
        assert len(dict_ret['flag']) == 0

    def test_create_get_req_friend_url_success(self):
        """Is a GET Request object created given a valid url?"""
        self.assertIsInstance(src.webcrawler.create_get_req(tests.test_const.FRIEND_HOME_URL),
                              urllib.request.Request)

    def test_create_post_req_fb_login_success(self):
        """Is a POST Request object created given a valid url?"""
        self.assertIsInstance(src.webcrawler.create_post_req(tests.test_const.FRIEND_HOME_URL, tests.test_const.LOGIN_DATA),
                              urllib.request.Request)

    def test_create_fb_absolute_url_success(self):
        """Is an absolute FB url created given a relative friend url?"""
        assert src.webcrawler.create_fb_absolute_url('/fakebook/50644342/') == \
               tests.test_const.FB_URL_PREFIX + '/fakebook/50644342/'


if __name__ == '__main__':
    unittest.main()
