__author__ = 'sweety'
# coding=utf-8
import requests
from PIL import Image
# import pyocr
# import pyocr.builders
from StringIO import StringIO
import lxml.etree as etree
import lxml.html.soupparser as soupparser
from bs4 import BeautifulSoup
# import sys


# tools = pyocr.get_available_tools()
# if len(tools) == 0:
#     print("No OCR tool found")
#     sys.exit(1)
# tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))
# langs = tool.get_available_languages()
# print("Available languages: %s" % ", ".join(langs))
# lang = langs[0]
# print("Will use lang '%s'" % (lang))

r = requests.get('http://my.51durian.com/website/index/init')
#print r._content
print r.cookies
print r.headers
tokenStr =  r.headers['set-cookie']
tokenStr = tokenStr[ : tokenStr.find(';')][11:]

cookies = dict(JSESSIONID=tokenStr)

r = requests.get('http://my.51durian.com/website/imageServlet?time=', cookies = cookies)
i = Image.open(StringIO(r.content))
# txt = tool.image_to_string(i, lang=lang, builder=pyocr.builders.TextBuilder())
# print 'txt is ', txt
i.show()
# file=open('/Users/sweety/Pictures/image.jpeg', "wb")
imageText = raw_input("input:")
r = requests.get('http://my.51durian.com/website/center/login?username=13991397719&password=76861624&validateCode='+imageText, cookies = cookies)
# r = requests.get('http://my.51durian.com/website/index/queryRegrecord', cookies = cookies)
r = requests.get('http://my.51durian.com/website/index/deptDoctor', cookies = cookies)
# url = '/website/center/addRegInfo?see_date=' +
# dom = soupparser.fromstring(r.text)

payload = {'depart_code': 'c1k', 'hp_code': 'sxfy', 'depart_name': u'产一科(曲)', 'employees_id': '14110515292929299634', 'employees_name': u'贺同强', 'employees_code': 'HTQ'}
r = requests.post('http://my.51durian.com/website/index/doctorReg', data = payload, cookies = cookies)
print r.text
soup = BeautifulSoup(r.text)
print soup.find(id='depart_code')
# for item in dom:
#     print item.tag

# for ele in dom.xpath('//a'):
#     print ele.tag