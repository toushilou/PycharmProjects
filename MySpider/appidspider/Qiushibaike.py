import urllib2
import urllib
import re
import thread
import time

class HTML_Tool:
    
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    EndCharToNoneRex = re.compile("<.*?>")
    BgnPartRex= re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]

    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)
        x = self.BgnPartRex.sub("\n    ",x)
        x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNextTabRex.sub("\t",x)
        x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
        return x

class HTML_Model:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.myTool = HTML_Tool()
        self.enable = False

    def GetPage(self,page):
        myUrl = "http://m.qiushibaike.com/hot/page/" + page
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER')
        opener = urllib2.build_opener()
        opener.addheaders = [headers]
        myResponse = opener.open(myUrl)
        myPage = myResponse.read()

        unicodePage = myPage.decode("utf-8")

        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            items.append([item[0].replace("\n",""), item[1].replace("\n","")])
        return items

    def LoadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print 'Could not access Qiushibaike!'
            else:
                time.sleep(1)

    def ShowPage(self,q,page):
        for items in q:
            print u'Page %d' % page, items[0]
            print self.myTool.Replace_Char(items[1])
            myInput = raw_input()
            if myInput == 'quit':
                self.enable = False
                break

    def Start(self):
        self.enable = True
        page = self.page

        print u'Please wait while loading...'

        thread.start_new_thread(self.LoadPage,())

        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1

print u"""
***********************************************
   Programming: Qiushibaike
   version: 0.1   
   Date: 2014/3/16
   Language: Python 2.7
   Operation: input quit to quit
   Function:Press enter to scan hot articles
***********************************************
"""

print u'Please press enter to scan Qiubai today'
raw_input(' ')
myModel = HTML_Model()
myModel.Start()

