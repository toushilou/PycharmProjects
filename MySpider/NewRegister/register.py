# coding=utf-8

import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup
import re
from DataTypes import *
import codecs
import json
import threading
import time, datetime
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
userInfoDict = {}
allDocName = []
allUserInfo = []

def loadAllInfo(isDocInfo):
    if isDocInfo:
        f = codecs.open('docinfo.properties', 'r', encoding='utf-8')
    else:
        f = codecs.open('UserInfo.properties', 'r', encoding='utf-8')
    for line in f:
        if line[0] == '#':
            continue
        array = line.split('=')
        if len(array) != 2:
            continue
        infoArray = array[1].split(',')
        if isDocInfo:
            docInfoDict[array[0]] = DoctorInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3], infoArray[4].strip('\n'))
            allDocName.append(array[0])
        else:
            userInfo = UserInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3], infoArray[4], infoArray[5].strip('\n'))
            allUserInfo.append(userInfo)




loadAllInfo(True)
loadAllInfo(False)

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
param['username'] = '51080219870305392x'
param['password'] = 'WZMfire0911'
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

def getTheropyTime(url, userInfo):

    docmName = userInfo.docName

    param = {}
    param['docmId'] = docInfoDict[docmName].docmId
    param['docmName'] = docmName
    param['docmSex'] = ''
    param['docmTitle'] = docInfoDict[docmName].docmTitle
    param['deptId'] = docInfoDict[docmName].deptId
    param['deptName'] = docInfoDict[docmName].deptName
    param['areaId'] = docInfoDict[docmName].areaId
    # auth = HTTPBasicAuth('130203198401271211', 'ydd0808')

    startTime = datetime.datetime(2016, 7, 18, 20, 29, 30)

    while datetime.datetime.now() < startTime:
        print 'Program not starting yet...'
        time.sleep(1)

    while True:
        r = requests.post(url=url, data=param, cookies=cookies)
        pattern = re.compile(r'^regClick')
        soup = BeautifulSoup(r.text)
        aDict = soup.find_all('a', onclick=pattern)
        validRegDate = False
        aDict.sort()
        for regClick in aDict:
            schmIdInfo = regClick['onclick']
            firstIndex = schmIdInfo.find('\'')
            lastIndex = schmIdInfo[firstIndex + 1:].find('\'')
            schmId = schmIdInfo[firstIndex + 1: firstIndex + lastIndex + 1]
            date = schmIdInfo[len(schmId) + 13: len(schmId) + 23]
            index = schmIdInfo.find(docInfoDict[docmName].deptName)
            workType = schmIdInfo[index + 9: index + 11]
            if userInfo.date == date and userInfo.workType == workType:
                validRegDate = True
                break
            else:
                print 'No specific date!'
        if validRegDate:
            break


    url = 'http://1.85.2.83/website/center/querytime'
    param = {}


    param['schmId'] = schmId

    subr = requests.post(url, cookies=cookies, params=param)

    if len(subr.text) != 0:
        s = json.loads(subr.text)
        if userInfo.date == date and userInfo.workType == workType:
            regInfo = {}
            regInfo['schmId'] = schmId
            regInfo['deptName'] = docInfoDict[docmName].deptName
            regInfo['docmName'] = docmName
            regInfo['regDate'] = date
            regInfo['workType'] = userInfo.workType
            regInfo['patientname'] = userInfo.name
            regInfo['telephone'] = userInfo.telephone
            regInfo['identitycard'] = userInfo.id
            regInfo['queueNum'] = s[0]['queueNum']
            regInfo['dataType'] = s[0]['dataType']
            regInfo['queueDate'] = s[0]['queueDate']
            regInfo['areaId'] = docInfoDict[docmName].areaId
            regInfo['docmId'] = docInfoDict[docmName].docmId
            regInfo['deptId'] = docInfoDict[docmName].deptId
            while not addRegInfo(regInfo, cookies):
                pass
            # print s[0]['dataType']
            # print docmName, date, s

def addRegInfo(regInfo, cookies):
    url = 'http://1.85.2.83/website/center/addRegInfo'

    r = requests.get(url, params=regInfo, cookies=cookies)
    print r.text

    return True if r.text[0] == '0' else False



for userInfo in allUserInfo:
    threading.Thread(getTheropyTime(url, userInfo))


