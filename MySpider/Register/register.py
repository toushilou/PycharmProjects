__author__ = 'sweety'

import requests

r = requests.get('http://my.51durian.com/website/index/init')
print r._content
tokenStr =  r.headers['set-cookie']
index = tokenStr.find(';')
tokenStr = tokenStr[ : index][11:]


imageText = raw_input("input:")
cookies = dict(JSESSIONID=tokenStr)

r = requests.get('http://my.51durian.com/website/center/login?username=18966865127&password=ydd0808&validateCode='+imageText, cookies = cookies)
print r._content

print tokenStr
