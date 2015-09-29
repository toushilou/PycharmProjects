__author__ = 'qyuan'

import requests

url = 'http://action.ldh.ldjt.com.cn/kidsvote/save.ashx'

headers = {}
headers['Host'] = 'action.ldh.ldjt.com.cn'
headers['Content-Length'] = '39'
headers['Accept'] = 'text/plain, */*; q=0.01'
headers['Origin'] = 'http://action.ldh.ldjt.com.cn'
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
headers['Connection'] = 'keep-alive'
headers['User-Agent'] ='Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.2.4 NetType/WIFI Language/zh_CN'
headers['Accept-Language'] = 'zh-cn'
headers['Referer'] = 'http://action.ldh.ldjt.com.cn/kidsvote/list.aspx?city=shx_1'
headers['Accept-Encoding'] = 'gzip, deflate'

# params = {}
# params['id'] = '145'

data = {}
data['id'] = '145'
data['uid'] = 'oAWFPt6oIIQ8G0YbXpohrXhNF5Ew'

cookies = {}
cookies['ASP.NET_SessionId'] = 'slkpndoblquervajkg2rw2lo'

r = requests.get(url, headers = headers, data = data, cookies = cookies)
print len('oAWFPt6oIIQ8G0YbXpohrXhNF5Ew')
print r.text