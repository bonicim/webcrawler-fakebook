from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        if tag != 'input':
            return
        # attrs is a list of Tuple name value pairs for a specific tag
        attr = dict(attrs) # a dictionary of name value pairs for a tag

        # linear search for csrf token
        for key in attr:
            # only add the dictionary containing csrf token
            if attr[key] == 'csrfmiddlewaretoken':
                self.links['csrf'] = attr
                break





