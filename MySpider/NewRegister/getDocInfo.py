# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
from DataTypes import *

url = 'http://101.254.212.167/website/index/deptDoctor'

params = {}
params['depart_code'] = '9d2d5b3c26e341e98a0700032bd4f67b'
params['depart_name'] = u'产三科(曲)'
params['area_id'] = 'newareaId'

r = requests.post(url, data=params)
soap = BeautifulSoup(r.text)
pattern = re.compile(r'^redirectPB')

allDocInfo = soap.find_all('a', onclick=pattern)
docInfoDict = {}

def loadAllDocInfo():
    f = open('docinfo.properties', 'r')
    for line in f:
        array = line.split('=')
        if len(array) != 2:
            continue
        infoArray = array[1].split(',')
        docInfoDict[array[0]] = DoctorInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3])

for docInfo in allDocInfo:
    # print docInfo['onclick']
    index = docInfo['onclick'][47:].find('\'')
    docmName = docInfo['onclick'][47:][:index]
    # print docmName
    title = docInfo['onclick'][47:][index + 6:][:docInfo['onclick'][47:][index + 6:].find('\'')]

    docmId = docInfo['onclick'][12:44]
    deptId = '9d2d5b3c26e341e98a0700032bd4f67b'

    print docmName + '=' + docmId + ',' + title + ',' + deptId + ',' + u'产三科(曲)' + ',42342f2132a7482b8e04667e5777dbb6'

