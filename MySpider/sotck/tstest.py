__author__ = 'sweety'
#coding=gbk
import tushare as ts
import pandas as pd
import requests
import sys
import urllib2
import scipy as sp
from HTMLParser import HTMLParser

#f = open('stock_basic', 'w')

df = ts.get_stock_basics()
#df.to_csv('stock_basic', encoding='gbk')
dates = pd.date_range('20150420', periods=6)


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == 'href':
                        if value.startswith('/stock/lhb/') and not value.startswith('/stock/lhb/yyb/'):
                            print value


if __name__ == "__main__":
    r = requests.get('http://data.eastmoney.com/stock/lhb.html')
    # r = urllib2.urlopen('http://data.eastmoney.com/stock/lhb.html').read()
    r = unicode(r._content,'GBK').encode('UTF-8')
    hp = MyHTMLParser()
    hp.feed(r)
    hp.close()
