__author__ = 'sweety'

import requests
from PIL import Image
# import pyocr
# import pyocr.builders
from StringIO import StringIO
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
file=open('/Users/sweety/Pictures/image.jpeg', "wb")
imageText = raw_input("input:")
r = requests.get('http://my.51durian.com/website/center/login?username=18966865127&password=ydd0808&validateCode='+imageText, cookies = cookies)
r = requests.get('http://my.51durian.com/website/index/queryRegrecord', cookies = cookies)
print r._content