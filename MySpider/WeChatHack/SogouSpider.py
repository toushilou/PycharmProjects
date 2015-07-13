__author__ = 'qyuan'
# coding=utf-8
import requests
import sys
from pymongo import MongoClient
from bs4 import BeautifulSoup
import json
import utils.Properties as properties
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
cookies = {}
cookies['SUID'] = 'F2FB20757B430E0A00000000508E4080'
cookies['SUV'] = '00A71A0F7520FBF250C9586038E6B476'
cookies['SMYUV'] = '1358296837075374'
cookies['ssuid'] = '7192526008'
cookies['pgv_pvi'] = '6435798016'
cookies['CXID'] = 'A84044F23F0795CB5C8AE198BE21C454'
cookies['browser_width'] = '1349'
cookies['browser_height'] = '643'
cookies['IPLOC'] = 'CN6101'
cookies['ABTEST'] = '0|1435634810|v1'
cookies['weixinIndexVisited'] = '1'
cookies['_ga'] = 'GA1.2.1719920014.1435720096'
cookies['SNUID'] = '526480D59FA58524CEAA48DBA0AEB407'
cookies['ld'] = 'p6VUIkllll2qALdMlllllVQ0g0olllllNvREDkllll9lllllRvoll5@@@@@@@@@@'
cookies['sct'] = '25'
keywordDic = properties.initPropers('./keyword')
url = 'http://weixin.sogou.com/weixin'
client = MongoClient('42.96.141.125',27017)
for k, v in keywordDic.items():
    queryStr = {}
    queryStr['query'] = v
    for x in xrange(1, 11):
        queryStr['page'] = x
        r = requests.get(url, params = queryStr, headers = headers, cookies = cookies)
        #print r._content.encode('gbk')
        soup = BeautifulSoup(r._content)
        mp_dic = {}
        db = client.testdb
        col = db[k]
        items = soup.find_all(attrs = 'txt-box')
        for item in items:
            #print item
            mp_name =  item.find(name = 'h3').text
            mp_number = item.find(name = 'span').text[4:]
            mp_description = item.find(name = 'span', attrs = {'class': 'sp-txt'}).text
            try:
                latest_article = item.find(name = 'a', attrs = {'class': 'blue'})['href']
                mp_biz = latest_article[len('http://mp.weixin.qq.com/s?__biz='):]
                index = mp_biz.find('&')
                mp_biz = mp_biz[:index]
                #print mp_biz
            except Exception, e:
                print e.message
                continue
            col.insert({'mp_name': mp_name, 'mp_number': mp_number, 'mp_description': mp_description, 'mp_biz': mp_biz})
            print 'done for ', k, 'page ', x
        time.sleep(30)
    print 'done for all ', k
    time.sleep(60)
# db = client.testdb
# col = db.news
# for i in col.find():
#     print i
