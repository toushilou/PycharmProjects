# coding=utf-8

import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup
import re
from DataTypes import *
import codecs
import json
from requests.auth import HTTPBasicAuth

# url = 'http://yy.nwwch.com/website/index/init'
# r = requests.post(url=url)
# tokenStr = r.headers['set-cookie']
# tokenStr = tokenStr[: tokenStr.find(';')][11:]
# auth = HTTPBasicAuth('332526198707290028', 'ydd0808')
# # url = 'http://yy.nwwch.com/website/center/querytime?schmId=1b0e11a486bc40b4a1b9df1204a3309f'
# url = 'http://yy.nwwch.com/website/index/doctorReg'
cookies = {}
# cookies['JSESSIONID'] = '1FA407F00CC5D875C46AFAE347D55F7F'
docInfoDict = {}
allDocName = []

def loadAllDocInfo():
    f = codecs.open('docinfo.properties', 'r', encoding='utf-8')
    for line in f:
        array = line.split('=')
        if len(array) != 2:
            continue
        infoArray = array[1].split(',')
        docInfoDict[array[0]] = DoctorInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3], infoArray[4].strip('\n'))
        allDocName.append(array[0])

loadAllDocInfo()

url = 'http://1.85.2.83/website/index/init'
r = requests.post(url=url)
tokenStr = r.headers['set-cookie']
tokenStr = tokenStr[ : tokenStr.find(';')][11:]
cookies = dict(JSESSIONID=tokenStr)
r = requests.get('http://1.85.2.83//website/imageServlet?time=', cookies=cookies)
i = Image.open(StringIO(r.content))
i.save('/tmp/' + 'test.jpeg')
imageText = raw_input('input for imageCode for :')
param = {}
param['username'] = '130203198401271211'
param['password'] = 'ydd0808'
param['validateCode'] = imageText
url = 'http://1.85.2.83/website/center/login'
r = requests.post(url, data=param, cookies=cookies)
url = 'http://1.85.2.83/website/index/doctorReg'

# headers = {}
# headers['Host'] = 'yy.nwwch.com'
# headers['Origin'] = 'http://yy.nwwch.com'
# headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
# headers['Referer'] = 'http://yy.nwwch.com/website/index/deptDoctor'
# headers['Upgrade-Insecure-Requests'] = '1'

def getTheropyTime(docmName, url, regTime):

    param = {}
    param['docmId'] = docInfoDict[docmName].docmId
    param['docmName'] = docmName
    param['docmSex'] = ''
    param['docmTitle'] = docInfoDict[docmName].docmTitle
    param['deptId'] = docInfoDict[docmName].deptId
    param['deptName'] = docInfoDict[docmName].deptName
    param['areaId'] = docInfoDict[docmName].areaId
    # auth = HTTPBasicAuth('130203198401271211', 'ydd0808')

    r = requests.post(url=url, data=param, cookies=cookies)
    pattern = re.compile(r'^regClick')
    # print r.text

    soup = BeautifulSoup(r.text)
    aDict = soup.find_all('a', onclick=pattern)


    url = 'http://1.85.2.83/website/center/querytime'
    param = {}

    for regClick in aDict:
        schmIdInfo = regClick['onclick']
        firstIndex = schmIdInfo.find('\'')
        lastIndex = schmIdInfo[firstIndex + 1:].find('\'')
        schmId = schmIdInfo[firstIndex + 1: firstIndex + lastIndex + 1]
        date = schmIdInfo[len(schmId) + 13: len(schmId) + 23]
        piriod = schmIdInfo[len(schmId) + 40: len(schmId) + 42]
        index = schmIdInfo.find(docInfoDict[docmName].deptName)
        type = schmIdInfo[index + 9: index + 11]
        param['schmId'] = schmId

        subr = requests.post(url, cookies=cookies, params=param)

        if len(subr.text) != 0:
            s = json.loads(subr.text)
            if regTime == date:
                regInfo = {}
                regInfo['schmId'] = schmId
                regInfo['deptName'] = docInfoDict[docmName].deptName
                regInfo['docmName'] = docmName
                regInfo['regDate'] = date
                regInfo['workType'] = workType
                regInfo['patientname'] = docInfoDict[docmName].name
                regInfo['telephone'] = telephone
                regInfo['identitycard'] = id
                regInfo['queueNum'] = queueNum
                regInfo['dateType'] = dateType
                regInfo['queueDate'] = queueDate
                regInfo['areaId'] = areaId
                regInfo['docmId'] = docmId
                regInfo['deptId'] = deptId
            print s[0]['dataType']
            print docmName, date, piriod, s

def addRegInfo(regInfo, cookies):
    url = 'http://1.85.2.83/website/center/addRegInfo'

    r = requests.get(url, params=regInfo, cookies=cookies)



for docmName in allDocName:
    getTheropyTime(docmName, url, '')

