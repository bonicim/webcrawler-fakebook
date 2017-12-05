from html.parser import HTMLParser
import copy

class MyHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.__csrf_token = ()
        self.__secret_flags = ()
        self.__data_actual = []
        self.__frozendata = ()

    def csrf_token(self):
        return self.__csrf_token

    def secret_flags(self):
        return tuple(filter(lambda data: 'FLAG' in data, self.__frozendata))

    def feed(self, data):
        super().feed(data)
        self.__frozendata = tuple(copy.deepcopy(self.__data_actual))
        self.__data_actual.clear()

    def add_flag(self, set_flag, flag):
        return set_flag.union(flag)

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
            self.handle_friend_url(attrs)

    def handle_data(self, data):
        self.__data_actual.append(data)

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

    def handle_friend_url(self, attrs):
        attr = dict(attrs)  # a dictionary of name value pairs for an 'a' tag with one href pair
        if len(attr) != 1:
            return
        if 'href' in attr and attr['href'].startswith('/fakebook/'):
            self.links.append(('href_friend_url', attr['href']))
            self.links['friend'] = attr
            # grab the value from the dictionary and append something to it, then update it again
            # do the same for flags
        else:
            return
