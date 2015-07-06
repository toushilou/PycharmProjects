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

class MPObject:
    def __init__(self, mp_name, mp_number, mp_description, mp_biz):
        self.mp_name = mp_name
        self.mp_number = mp_number
        self.mp_description = mp_description
        self.mp_biz = mp_biz


mp_dic = {}
for item in soup.find_all(attrs = 'txt-box'):
    print item
    mp_name =  item.find(name = 'h3').text
    mp_number = item.find(name = 'span').text[4:]
    mp_description = item.find(name = 'span', attrs = {'class': 'sp-txt'}).text
    try:
        latest_article = item.find(name = 'a', attrs = {'class': 'blue'})['href']
        mp_biz = latest_article[len('http://mp.weixin.qq.com/s?__biz='):]
        index = mp_biz.find('&')
        mp_biz = mp_biz[:index]
        print mp_biz
    except Exception, e:
        print e.message
        continue
    mp_object = MPObject(mp_name, mp_number, mp_description, mp_biz)
    mp_dic[mp_name] = mp_object
