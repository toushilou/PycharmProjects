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
from bs4 import BeautifulSoup
import re
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
paragraphDict = {}
def loadAllDocInfo():
    f = open('docinfo.properties', 'r')
    for line in f:
        array = line.split('=')
        if len(array) != 2:
            continue
        infoArray = array[1].split(',')
        docInfoDict[array[0]] = DoctorInfo(array[0], infoArray[0], infoArray[1], infoArray[2], infoArray[3])

def loadParagraphInfo():
    f = open('paragraph.properties', 'r')
    for line in f:
        array = line.split('=')
        if len(array) != 2:
            continue
        paragraphDict[array[0]] = array[1].strip()

loadAllDocInfo()
loadParagraphInfo()
userinfo = UserInfo('18966865127', '詹惠疏', 'ydd0808', '2015-07-01', '09:00', '10:00', '贺译平')
docInfo = docInfoDict[userinfo.docName]
print paragraphDict[userinfo.start]
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


isReady = False
payload = {'depart_code': docInfo.dept, 'hp_code': 'sxfy', 'depart_name': docInfo.deptName, 'employees_id': docInfo.id, 'employees_name': docInfo.name, 'employees_code': docInfo.code}
pattern = re.compile(r'^reg_a_')
while not isReady:
    r = requests.post('http://my.51durian.com/website/index/doctorReg', data = payload, cookies = cookies)
    soup = BeautifulSoup(r.text)
    reg_id_list = soup.find_all(id=pattern)
    reg_id = None
    for item in reg_id_list:
        if userinfo.date in item['onclick']:
            reg_id = item['id'][6:]
            isReady = True
            break
    if not isReady:
        print 'The new registration hasn\'t been released!'

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
           'schema_id': reg_id, 'depart_code': docInfo.dept, 'depart_name': docInfo.deptName, 'employees_code': docInfo.code,
           'employees_name': docInfo.name, 'oper_code': oper_code,
           'start_paragraph': userinfo.start, 'end_paragraph': userinfo.end,
           'paragraph_id':paragraphDict[userinfo.start], 'hp_code': 'sxfy'}
url ='http://my.51durian.com/website/center/addRegInfo'
r = requests.post(url, params=payload, cookies = cookies)
print r.text

# print r.text
# for item in dom:
#     print item.tag

# for ele in dom.xpath('//a'):
#     print ele.tag