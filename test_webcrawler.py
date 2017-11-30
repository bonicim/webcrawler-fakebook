import unittest
import webcrawler


class WebcrawlerTestCase(unittest.TestCase):
    """ Tests for webcrawler.py.
    All functions beginning with test will be run when unittest.main() is called. """

    def test_is_five_five(self):
        self.assertTrue(webcrawler.is_5(5))


if __name__ == '__main__':
    unittest.main()
