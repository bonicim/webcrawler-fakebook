import unittest
import webcrawler


class WebcrawlerTestCase(unittest.TestCase):
    """ Tests for webcrawler.py.
    All functions beginning with test will be run when unittest.main() is called. """

    USERNAME = 'bonicillo.m'
    PASSWORD = 'toast'
    REL_FRIEND_URL = ''
    FRIEND_URL = ''
    FRIEND_PAGE_URL = ''

    # TODO Write tests
    def test_getopts_returns_username_password(self):
        """Is a diciontary containing username and password retrieved?"""
        pass

    def test_getopts_returns_error(self):
        """Does error get returned if 0, 1, or 3 more arguments are given?"""
        pass

    def test_login_fakebook_success(self):
        """Does a valid user's fakebook profile get returned?"""
        pass

    def test_login_fakebook_failure(self):
        """Does an error page for an invalid fakebook profile get returned?"""
        pass

    def test_open_friend_page_success(self):
        """Does a valid fakebook landing page of a friend get returned?"""
        pass

    def test_open_friend_page_failure(self):
        """Does an error page for an invalid fakebook profile get returned?"""
        pass

    def test_open_view_friends_page_success(self):
        """Does a fakebook view friends page of a valid friend get returned?"""
        pass

    def test_open_view_friends_page_failure(self):
        """Does an error page for an invalid view friends url get returned?"""
        pass

    def test_parse_flags_friends_nextpage_success(self):
        """Does a dictionary containing 3 key value pairs get returned?"""
        pass

    def test_parse_flags_friends_nextpage_no_next(self):
        """Does a dictionary containing 3 key value pairs in which the next_page key has
        an empty list get returned?"""
        pass

    def test_parse_flags_friends_nextpage_no_flag(self):
        """Does a dictionary containing 3 key value pairs in which the flags key has
        an empty list get returned?"""
        pass

    def test_parse_flags_friends_nextpage_no_friends(self):
        """Does a dictionary containing 3 key value pairs in which the friends key has
        an empty list get returned?"""
        pass

    def test_create_get_req_friend_url_success(self):
        """Is a Request object created given a valid url?"""
        pass

    def test_create_post_req_fb_login_success(self):
        """Is a Post object created given a valid url?"""
        pass

    def test_create_fb_absolute_url_success(self):
        """Is an absolute FB url created given a relative friend url?"""
        pass


if __name__ == '__main__':
    unittest.main()
