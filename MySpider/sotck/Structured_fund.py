__author__ = 'sweety'
# coding=utf-8
import sys
import requests
import chardet
from ghost import Ghost
import BeautifulSoup


reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://www.abcfund.cn/style/fundlist.php'

ghost = Ghost()
session = ghost.start()
page, extra_resources = session.open(url)
print session.content
# f = open('funddata')
# data = ''
# for line in f:
#     data = line
# print data
#soup = BeautifulSoup(data)
#print soup.get_text()
# text = session.evaluate("document.getElementByTagName('tbody').getAttribute('style');")
#print soup.get_text()
# r = requests.get(url)
# print chardet.detect(r._content)
# print (r._content).decode('GB2312')


#soup = BeautifulSoup(r._content)
