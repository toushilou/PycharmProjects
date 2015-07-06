# coding:utf-8
import web, urllib2, json
import sys
import hashlib
from xml.etree import ElementTree as ET
import os
import time
default_encoding = 'utf-8' 
if sys.getdefaultencoding() != default_encoding: 
    reload(sys) 
    sys.setdefaultencoding(default_encoding) 
urls = (
    '/', 'index',
    '/test', 'index1',
    '/getkey', 'getkey'
    )

app = web.application(urls, globals(), autoreload=True)
class index:
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = 'yuanquan'
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode =sha1.hexdigest()
        if hashcode == signature:
            return echostr
        else:
            return 'Error'
        
    def POST(self):
        str_xml = web.data() 
        xml = ET.fromstring(str_xml)
        content = xml.find("Content").text
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        if content == 'test':
            return self.render.reply_articles(fromUser,
                                   toUser,int(time.time()),
                                   title='my test title',
                                   description='test description',
                                   picurl='http://pica.nipic.com/2007-11-09/2007119124513598_2.jpg',
                                   url='http://www.madfinger.club/getkey')
        return self.render.reply_text(fromUser,toUser,int(time.time()),'I am under developed and have no other functions. You were saying:' + content + " and toUser id is " + toUser + " from user id is " + fromUser)
        
class index1:
    def GET(self):
        web.header('Content-Type', 'text/plain; charset=utf-8') 
        referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
        raise web.seeother(referer)
        return u'你好 test!'

class getkey:
    def GET(self):
        data = web.input()
        for k,v in data.items():
            print k, '==', v

application = app.wsgifunc()

    
if __name__ == "__main__":
    app.run()
