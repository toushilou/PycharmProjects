__author__ = 'qyuan'
# coding=utf-8
import requests
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http://weixin.sogou.com/weixin'
queryStr = {}
queryStr['query'] = u'新闻'
r = requests.get(url, params = queryStr)
soup = BeautifulSoup(r._content)
for item in soup.find_all(attrs = 'txt-box'):
    print item.encode('gbk')
    name =  item.find(name='h3').encode('gbk')
    number = item.find(attrs='span')
    print number

