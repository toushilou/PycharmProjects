import urllib2, re, HTMLParser

host = "http://desk.zol.com.cn"
localSavePath = "d:\girls"
startHtmlUrl = ''
htmlUrlList = []
imageUrlList = []

def downloadImage(url)
    patter = '[0-9]*\.jpg'
    match = re.search(patter, url)
    if match:
        cont = urllib2.urlopen(url).read()
        print 'downloading...', match.group()
        filename = localSavePath + match.group()
        f = open(filename, "w+")
        f.write(cont)
        f.close()
    else:
        print 'no match'
    
def getImageUrlByHtmlUrl(htmlUrl)
    parser = MyHtmlParse(False)
    request = urllib2.Request(htmlUrl)
    try:
        response = urllib2.urlopen(request)
        content = response.read()
        parser.feed(content)
    expect urllib2.URLError, e:
        print e.reason
    
class MyHtmlParser(HTMLParser.HTMLParser):
    def __init__(self,isIndex):
        self.isIndex = isIndex
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if(self.isIndex):
            if(tag == 'a'):
                if(len(attr) == 4):
                    if(attr[0]) == ('class', 'pic')):
                        newUrl = host+attrs[1][1]
                        print 'find a picture link:',newUrl
                        global startHtml
                        startHtmlUrl = newUrl
                        getImageUrlByHtmlUrl(newUrl)
                        
        
