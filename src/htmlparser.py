from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    #TODO: implement
    def handle_data(self, data):
        super().handle_data(data)

    def get_starttag_text(self):
        return super().get_starttag_text()

    def handle_startendtag(self, tag, attrs):
        super().handle_startendtag(tag, attrs)

    def handle_endtag(self, tag):
        super().handle_endtag(tag)