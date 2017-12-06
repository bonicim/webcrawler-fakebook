from html.parser import HTMLParser
import copy

class MyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.__csrf_token = ()
        self.__secret_flags = ()
        self.__data_actual = []
        self.__frozendata = ()
        self.__friends = ()
        self.__pagelist = ()

    def csrf_token(self):
        return self.__csrf_token

    def secret_flags(self):
        return tuple(filter(lambda data: 'FLAG' in data, self.__frozendata))

    def friends(self):
        return self.__friends

    def pagelist(self):
        return self.__pagelist

    def feed(self, data):
        self.flush_accumulators()
        super().feed(data)
        self.__frozendata = tuple(copy.deepcopy(self.__data_actual))

    def flush_accumulators(self):
        self.__csrf_token = ()
        self.__secret_flags = ()
        self.__data_actual.clear()
        self.__friends = ()
        self.__pagelist = ()

    def handle_data(self, data):
        self.__data_actual.append(data)

    def handle_startendtag(self, tag, attrs):
        if tag != 'input':
            return
        attr = dict(attrs)
        self.parse_csrf(attr)

    def parse_csrf(self, attr):
        if 'csrfmiddlewaretoken' in attr.values():
            self.__csrf_token = (attr['value'],)

    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.parse_secret_flag(attrs)
        elif tag == 'a':
            self.parse_friend_url(attrs)
            self.parse_viewing_friends_links(attrs)

    def parse_secret_flag(self, attrs):
        attr = dict(attrs)  # a dictionary of name value pairs for a tag
        if len(attr) != 2:
            return
        if self.is_secret_flag(attr):
            # TODO Must find a way to verify that FLAG values are contained within secret flag
            pass

    def is_secret_flag(self, attr):
        return ('class' in attr and attr['class'] == 'secret flag') and \
               ('style' in attr and attr['style'] == 'color:red')

    def parse_friend_url(self, attrs):
        attr = dict(attrs)  # a dictionary of name value pairs for an 'a' tag
        if len(attr) != 1:  # a tags that we care about should only have one name value pair
            return
        if self.is_href_fakebook_friend_url(attr):
            self.__friends = self.__friends + (attr['href'],)

    def is_href_fakebook_friend_url(self, attr):
        return 'href' in attr and \
               attr['href'].startswith('/fakebook/') and \
               len(attr['href']) > 10 and \
                'friends' not in attr['href']

    def parse_viewing_friends_links(self, attrs):
        attr = dict(attrs)  # a dictionary of name value pairs for an 'a' tag
        if len(attr) != 1:  # a tags that we care about should only have one name value pair
            return
        if self.is_href_pagelist_friends(attr):
            self.__pagelist = self.__pagelist + (attr['href'],)

    def is_href_pagelist_friends(self, attr):
        # looks for links that are of the form
        # '/fakebook/<some id>/friends/<some number>' and the last letter is a digit
        return 'href' in attr and \
               attr['href'].startswith('/fakebook/') and \
               'friends' in attr['href'] and \
               len(attr['href']) >= len('/fakebook/friends/1') and \
               attr['href'][-2].isdigit()

