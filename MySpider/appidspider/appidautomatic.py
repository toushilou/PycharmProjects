__author__ = 'qyuan'

import requests
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.id = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "body":
            if len(attrs) == 0: pass
            else:
                print tag

version = ''
cookies = dict(JSESSIONID='8E471F4FD75C1E322448B8A26FBD5753')
r = requests.get('https://www.baidu.com', cookies = cookies)
#r = requests.get('http://spaces.telenav.com:8080/display/biz/Application+Repository', cookies = cookies, stream = True)
parser = MyHTMLParser()
parser.feed(r.text)
#print r._content