import src.my_htmlparser
import unittest
import pytest
from tests.util_test import SECRET_FLAG_LEN
from tests.util_test_html import FAKEBOOK_LOGIN_YES_FLAG_HTML, FAKEBOOK_LOGIN_YES_3_FLAG_HTML,\
	FAKEBOOK_LOGIN_YES_4_FLAG_HTML, FAKEBOOK_LOGIN_HTML, MEMBER_LANDING_HTML, \
	FRIEND_LANDING_HTML, FRIEND_VIEWING_FRIENDS_HTML, FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML
my_htmlparser = src.my_htmlparser.MyHTMLParser()


class WebcrawlerTestCase(unittest.TestCase):

	def test_parse_flag_where_flag_present(self):
		"""Does a list of one flag get returned?"""
		my_htmlparser.feed(FAKEBOOK_LOGIN_YES_FLAG_HTML)
		flag_tuple = my_htmlparser.secret_flags()
		self.assertIsNotNone(flag_tuple)
		for flag in flag_tuple:
			assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN

	def test_parse_flag_where_multi_flag_present(self):
		"""Does a list of three flags get returned?"""
		my_htmlparser.feed(FAKEBOOK_LOGIN_YES_3_FLAG_HTML)
		flag_tuple = my_htmlparser.secret_flags()
		self.assertIsNotNone(flag_tuple)
		assert len(flag_tuple) == 3
		for flag in flag_tuple:
			assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN

		my_htmlparser.feed(FAKEBOOK_LOGIN_YES_4_FLAG_HTML)
		flag_tuple = my_htmlparser.secret_flags()
		self.assertIsNotNone(flag_tuple)
		assert len(flag_tuple) == 4
		for flag in flag_tuple:
			assert len(flag.split(':')[1].strip()) == SECRET_FLAG_LEN

	def test_parse_flag_where_flag_absent(self):
		"""Does an empty list get returned?"""
		my_htmlparser.feed(FAKEBOOK_LOGIN_HTML)
		flag_tuple = my_htmlparser.secret_flags()
		self.assertIsNotNone(flag_tuple)
		assert len(flag_tuple) == 0

	def test_parse_friend_where_friends_present(self):
		"""Does a list of friend url's get returned?"""
		my_htmlparser.feed(MEMBER_LANDING_HTML)
		tup_friend_url = my_htmlparser.friends()
		self.assertIsNotNone(tup_friend_url)
		assert len(tup_friend_url) == 10
		assert '/fakebook/190909169/' in tup_friend_url

		my_htmlparser.feed(FRIEND_VIEWING_FRIENDS_HTML)
		tup_friend_url = my_htmlparser.friends()
		self.assertIsNotNone(tup_friend_url)
		assert len(tup_friend_url) > 0
		assert '/fakebook/89081356/' in tup_friend_url

	def test_parse_friend_where_no_friends_except_user(self):
		"""Does an empty list get returned?"""
		my_htmlparser.feed(FRIEND_LANDING_HTML)
		tup_friend_url = my_htmlparser.friends()
		self.assertIsNotNone(tup_friend_url)
		assert len(tup_friend_url) == 1

		my_htmlparser.feed(FAKEBOOK_LOGIN_HTML)
		tup_friend_url = my_htmlparser.friends()
		self.assertIsNotNone(tup_friend_url)
		assert len(tup_friend_url) == 0

	def test_parse_next_page_where_next_exists(self):
		"""Does a dictionary containing 3 key value pairs in which the next_page key has
		an empty list get returned?"""
		# Case 1: Friend viewing friends page
		my_htmlparser.feed(FRIEND_VIEWING_FRIENDS_HTML)
		tup_next_page = my_htmlparser.pagelist()
		self.assertIsNotNone(tup_next_page)
		assert len(tup_next_page) > 0
		assert len(tup_next_page) == 3
		for url in tup_next_page:
			assert len(url) > len('/fakebook/996350946/')
		assert '/fakebook/996350946/friends/2/' in tup_next_page

		# Case 2: Landing page of friend where the next page must be the first page
		my_htmlparser.feed(FRIEND_LANDING_HTML)
		tup_next_page = my_htmlparser.pagelist()
		self.assertIsNotNone(tup_next_page)
		assert len(tup_next_page) == 1
		for url in tup_next_page:
			assert len(url) > len('/fakebook/996350946/')
		assert '/fakebook/996350946/friends/1/' in tup_next_page

	def test_parse_next_page_where_next_absent(self):
		"""Does a dictionary containing 3 key value pairs get returned?"""
		# Case 1: My Landing page has no next links because I have few friends
		my_htmlparser.feed(MEMBER_LANDING_HTML)
		tup_next_page = my_htmlparser.pagelist()
		self.assertIsNotNone(tup_next_page)
		assert len(tup_next_page) == 0

		# Case 2: The last page of a friend's list of friends. There is no next.
		my_htmlparser.feed(FRIEND_VIEWING_FRIENDS_LAST_PAGE_HTML)
		tup_next_page = my_htmlparser.pagelist()
		self.assertIsNotNone(tup_next_page)
		assert len(tup_next_page) > 0
		for url in tup_next_page:
			assert len(url) > len('/fakebook/996350946/')

