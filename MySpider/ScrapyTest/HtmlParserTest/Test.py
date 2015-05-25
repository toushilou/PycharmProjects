__author__ = 'qyuan'
import HTMLParser
def findUrls( text ):
  class URLFinder(HTMLParser.HTMLParser):
     urls=[]
     def handle_starttag(self, tag, attrs):
         if tag == 'a':
            self.urls.append( dict(attrs).get('href','') )
  f = URLFinder()
  f.feed( text )

