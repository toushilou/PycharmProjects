#coding: utf-8 #############################################################
# File Name: girls.py
# Author: mylonly
# mail: mylonly@gmail.com
# Created Time: Mon 09 Jun 2014 09:23:18 PM CST
#########################################################################
#!/usr/bin/python

import urllib2,HTMLParser,re

#根url
host = "http://desk.zol.com.cn"
#本地保存地址
localSavePath = 'd:\\girls\\'
#起始图片html地址
startHtmlUrl = ''
#图片页Html的地址
htmlUrlList = []
#图片Url地址
imageUrlList = []
#根据得到的图片路径URL将图片下载下来保存本地
def downloadImage(url):
	cont = urllib2.urlopen(url).read()
	patter = '[0-9]*\.jpg';
	match = re.search(patter,url);
	if match:
		print 'downloading the file:',match.group()
		filename = localSavePath+match.group()
		f = open(filename,'wb')
		f.write(cont)
		f.close()
	else:
		print 'no match'

#根据首页得到的图片集遍历每个图片集
def getImageUrlByHtmlUrl(htmlUrl):
	parser = MyHtmlParse(False)
	request = urllib2.Request(htmlUrl)
	try:
		response = urllib2.urlopen(request)
		content = response.read()
		parser.feed(content)
	except urllib2.URLError,e:
		print e.reason

class MyHtmlParse(HTMLParser.HTMLParser):
	def __init__(self,isIndex):
		self.isIndex = isIndex;
		HTMLParser.HTMLParser.__init__(self)
	def handle_starttag(self,tag,attrs):
		if(self.isIndex):
			if(tag == 'a'):
				if(len(attrs) == 4):
					if(attrs[0] ==('class','pic')):
						newUrl = host+attrs[1][1]
						print 'find a picture link:',newUrl
						startHtmlUrl = newUrl
						getImageUrlByHtmlUrl(newUrl)
		else:
			if(tag == 'img'):
				if(attrs[0] == ('id','bigImg')):
						imageUrl = attrs[1][1]
						print 'find a picture:',imageUrl
						downloadImage(imageUrl)
						#imageUrlList.append(imageUrl)	
			if (tag == 'a'):
				if (len(attrs) == 4):
					if (attrs[1] == ('class','next')):
						nextUrl = host + attrs[2][1]
						print 'find a webpage link for a picture:',nextUrl
						global startHtmlUrl
						if (startHtmlUrl != nextUrl):
							getImageUrlByHtmlUrl(nextUrl)
#分析首页得到每个图片集的链接
indexUrl = 'http://desk.zol.com.cn/meinv/'
m = urllib2.urlopen(indexUrl).read()
parserIndex = MyHtmlParse(True)
parserIndex.feed(m)