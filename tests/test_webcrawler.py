import unittest
import pytest
import webcrawler
import tests.util_test
import urllib.request
import tests.util_test_html
import src.my_htmlparser
from tests.util_test import SECRET_CSRF_LEN, ARGV, FB_LOGIN_URL, FB_URL_PREFIX, FRIEND_HOME_URL, \
	LOGIN_DATA
from tests.util_test_html import FAKEBOOK_LOGIN_YES_3_FLAG_HTML, MEMBER_LANDING_YES_FLAG_HTML, \
	MEMBER_LANDING_HTML, FRIEND_LANDING_HTML, FRIEND_VIEWING_FRIENDS_HTML, \
	FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML
my_htmlparser = src.my_htmlparser.MyHTMLParser()


class WebcrawlerTestCase(unittest.TestCase):
	""" Tests for webcrawler.py. All functions beginning with test will be run when unittest.main()
	is called. """
	def test_getopts_returns_username_password(self):
		"""Is a list containing username and password retrieved?"""
		assert webcrawler.getopts(ARGV) == ['bonicillo.m', 'toast']

	def test_getopts_returns_error(self):
		"""Does error get returned if 0, 1, or 3 more arguments are given?"""
		with self.assertRaises(SystemExit):
			webcrawler.getopts(['toast'])

	def test_login_fakebook_success(self):
		"""Does a valid user's fakebook profile get returned?"""
		# TODO
		pytest.skip()

	def test_login_fakebook_failure(self):
		"""Does an error page for an invalid fakebook profile get returned?"""
		# TODO
		pytest.skip()

	def test_get_all_friends_flags_not_empty(self):
		"""Does a valid fakebook landing page of a friend get returned?"""
		# TODO
		pytest.skip()
		friend_list, flag_list = webcrawler.get_all_friends_flags(tests.util_test.FRIEND_HOME_URL,
																  tests.util_test.init_opener())
		self.assertIsNotNone(friend_list)
		self.assertIsNotNone(flag_list)
		assert len(flag_list) == 0
		assert len(friend_list) == 86

	def test_parse_csrf_success(self):
		"""Does a CSRF token get returned when landing on the login page?"""
		parser = tests.util_test.init_parser()
		opener = tests.util_test.init_opener()
		csrf = webcrawler.get_csrf_token(opener, parser, FB_LOGIN_URL)
		self.assertIsNotNone(csrf)
		assert len(csrf) == SECRET_CSRF_LEN

	def test_create_get_req_friend_url_success(self):
		"""Is a GET Request object created given a valid url?"""
		self.assertIsInstance(webcrawler.create_get_req(FRIEND_HOME_URL), urllib.request.Request)

	def test_create_post_req_fb_login_success(self):
		"""Is a POST Request object created given a valid url?"""
		self.assertIsInstance(webcrawler.create_post_req(FRIEND_HOME_URL, LOGIN_DATA), urllib.request.Request)

	def test_create_fb_absolute_url_success(self):
		"""Is an absolute FB url created given a relative friend url?"""
		assert webcrawler.create_fb_absolute_url('/fakebook/50644342/') == FB_URL_PREFIX + '/fakebook/50644342/'

	def test_parse_flags_friends_pagelist(self):
		# Case 1: Member homepage
		dict_ret = webcrawler.parse_flags_friends_page_list(MEMBER_LANDING_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 0
		assert len(dict_ret['friends']) == 10
		assert len(dict_ret['page_list']) == 0

		# Case 2: Friend homepage
		dict_ret = webcrawler.parse_flags_friends_page_list(FRIEND_LANDING_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 0
		assert len(dict_ret['friends']) == 1
		assert len(dict_ret['page_list']) == 1

		# Case 3: View Friends List
		dict_ret = webcrawler.parse_flags_friends_page_list(
			FRIEND_VIEWING_FRIENDS_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 0
		assert len(dict_ret['friends']) == 21
		assert len(dict_ret['page_list']) == 3

		# Case 4: View Friends Last Page
		dict_ret = webcrawler.parse_flags_friends_page_list(
			FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 0
		assert len(dict_ret['friends']) == 15
		assert len(dict_ret['page_list']) == 3

		# Case 5: Login Form Page
		dict_ret = webcrawler.parse_flags_friends_page_list(
			FAKEBOOK_LOGIN_YES_3_FLAG_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 3
		assert len(dict_ret['friends']) == 0
		assert len(dict_ret['page_list']) == 0

		# Case 6: View Friends Last Page with Flags
		dict_ret = webcrawler.parse_flags_friends_page_list(
			MEMBER_LANDING_YES_FLAG_HTML, my_htmlparser)
		self.assertIsNotNone(dict_ret)
		assert len(dict_ret) == 3
		assert len(dict_ret['flags']) == 1
		assert len(dict_ret['friends']) == 10
		assert len(dict_ret['page_list']) == 0


if __name__ == '__main__':
	unittest.main()
