__author__ = 'sweety'
# coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from PIL import Image
# import pyocr
# import pyocr.builders
from StringIO import StringIO
import lxml.etree as etree
import lxml.html.soupparser as soupparser
from bs4 import BeautifulSoup
import re
import urllib
from DataTypes import *
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
docInfoDict = {}
def loadAllDocInfo():
    f = open('docinfo.properties', 'r')
    for line in f:
        array = line.split('=')
        if len(array) != 2:
            continue
        infoArray = array[1].split(',')
        docInfoDict[array[0]] = DoctorInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3])

loadAllDocInfo()
userinfo = UserInfo('13991397719', '袁泉', '76861624', '2015-06-26', '9:00', '贺同强')
docInfo = docInfoDict[userinfo.docName]

r = requests.get('http://my.51durian.com/website/index/init')
#print r._content
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
params = {'username': userinfo.id, 'password': userinfo.password, 'validateCode': imageText}
r = requests.get('http://my.51durian.com/website/center/login', params = params, cookies = cookies)
print r.url
# r = requests.get('http://my.51durian.com/website/index/queryRegrecord', cookies = cookies)
r = requests.get('http://my.51durian.com/website/index/deptDoctor', cookies = cookies)
# url = '/website/center/addRegInfo?see_date=' +
# dom = soupparser.fromstring(r.text)

payload = {'depart_code': docInfo.getDept(), 'hp_code': 'sxfy', 'depart_name': docInfo.getDeptName(), 'employees_id': docInfo.getId(), 'employees_name': docInfo.getName(), 'employees_code': docInfo.getCode()}
r = requests.post('http://my.51durian.com/website/index/doctorReg', data = payload, cookies = cookies)
# print r.text
soup = BeautifulSoup(r.text)
pattern = re.compile(r'^reg_a_')
reg_id_list = soup.find_all(id=pattern)
reg_id = None
for item in reg_id_list:
    if userinfo.date in item['onclick']:
        reg_id = item['id'][6:]
        break
if reg_id == None:
    pass
oper_code_list = soup.find(id='patientselect')
patientList =  oper_code_list.contents
oper_code = None
for patient in patientList:
    if hasattr(patient, 'contents'):
        if str(patient.next) == userinfo.name:
            oper_code = str(patient)[15:32]
            print oper_code
            break

if oper_code == None:
    pass
# print reg_id
payload = {'see_date': userinfo.date, 'noon_code': '', 'name': userinfo.name,
           'schema_id': reg_id, 'depart_code': docInfo.getDept, 'depart_name': docInfo.getDeptName, 'employees_code': docInfo.getCode,
           'employees_name': docInfo.getName(), 'oper_code': oper_code,
           'start_paragraph': '10:00', 'end_paragraph': '11:00',
           'paragraph_id':'14120817273127319129', 'hp_code': 'sxfy'}
url ='http://my.51durian.com/website/center/addRegInfo'
r = requests.post(url, params=payload, cookies = cookies)
print r.url

# print r.text
# for item in dom:
#     print item.tag

# for ele in dom.xpath('//a'):
#     print ele.tag