__author__ = 'qyuan'

import requests
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.id = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "span":
            if len(attrs) == 0: pass
            else:
                print attrs

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#            'refer': 'http://spaces.telenav.com:8080/login.action?logout=true',
#            'Connection': 'keep-alive',
#            'Content-Length': '93',
#            'Cache-Control':'max-age=0',
#            'Origin': 'http://spaces.telenav.com:8080',
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'Accept-Encoding': 'gzip, deflate',
#            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2,ja;q=0.2,es;q=0.2,de-DE;q=0.2,de;q=0.2'
#            }


def getJsessionId(headers):
    jsessionidStr =  headers['set-cookie']
    beginIndex = jsessionidStr.index('=') + 1
    endIndex = jsessionidStr.index(';')
    jsessionid = jsessionidStr[beginIndex : endIndex]
    return jsessionid

r = requests.get('http://spaces.telenav.com:8080/login.action');
jsessionid = getJsessionId(r.headers)
print r.headers
# cookies = dict(JSESSIONID=jsessionid,
#                os_username='qyuan@telenavsoftware.com',
#                os_password='541236987Mar',
#                login='Log+in')
# r = requests.post('http://spaces.telenav.com:8080/dologin.action', cookies = cookies)
# r = requests.get('http://spaces.telenav.com:8080/', cookies = cookies)
# cookies =  dict(JSESSIONID=jsessionid)
# r = requests.get('http://spaces.telenav.com:8080/dashboard.action', cookies = cookies)
# parser = MyHTMLParser()
# parser.feed(r.text)
# print r._content

