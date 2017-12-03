from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        if tag != 'input':
            return
        # attrs is a list of Tuple name value pairs for a specific tag
        attr = dict(attrs) # a dictionary of name value pairs for a tag

        # name value pairs for each tag that we care about
        for key in attr:
            # only add the dictionary containing csrf token for any and all input tags
            if attr[key] == 'csrfmiddlewaretoken':
                self.links['csrf'] = attr
                break

    def handle_starttag(self, tag, attrs):
        if tag == 'h2':
            self.handle_secret_flag(attrs)

    def handle_data(self, data):
        self.data_actual.append(data)

    def handle_secret_flag(self, attrs):
        attr = dict(attrs) # a dictionary of name value pairs for a tag
        if len(attr) != 2:
            return
        if ('class' in attr and attr['class'] == 'secret flag') and ('style' in attr and attr['style'] == 'color:red'):
            self.links['secret_flag'] = attr
        else:
            return

