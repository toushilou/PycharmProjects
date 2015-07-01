__author__ = 'qyuan'
# coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = u'http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FPiajxSqBRaELj042tUfsS4IUv3wibNLH18vhib0YtmmQ1V7zwvXWPrGPdYgia4qkktIKubXP9KFXzQsWBubGbBg7iag%2F0'.replace('%2F','/')
url = url.replace('%3A',':')
print url
cookies = {}
cookies['pgv_pvi'] = '41287680'
cookies['pgv_pvid'] = '9917116262'
cookies['sd_cookie_crttime'] = '1430731556250'
cookies['sd_userid'] = '26151430731556250'
cookies['tencentvideo_face'] = 'http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FPiajxSqBRaELj042tUfsS4IUv3wibNLH18vhib0YtmmQ1V7zwvXWPrGPdYgia4qkktIKubXP9KFXzQsWBubGbBg7iag%2F0'
cookies['tencentvideo_nick'] = '%E8%A2%81%E6%B3%89'
cookies['tencentvideo_openid'] = 'o-I78jntfAhcGrpPmw722lIj2sbw'
cafile = 'cacert.pem'
wxurl = 'https://mp.weixin.qq.com/mp/getappmsgext'
params = {}
params['__biz'] = 'MzA4MjA0OTEwMQ=='
params['mid'] = '221566822'
params['sn'] = '24843dabf723b6a41e995eb1adfb2453'
params['idx'] = '1'
params['scene'] = ''
params['title'] = u'【谜题】智商没有135连个广告都看不懂'
params['ct'] = '1435723811'
params['devicetype'] = 'iPhone&nbsp;OS8.3'
params['version'] = ''
params['f'] = 'json'
params['r'] = '0.3998817664105445'
params['is_need_ad'] = '1'
params['comment_id'] = '0'
params['is_need_reward'] = '0'
params['both_ad'] = '0'
params['reward_uin_count'] = '0'
params['uin'] = 'MjYxMzkyMDM1'
params['key'] = 'af154fdc40fed003f97328c0686af3643bad92d8140bb4d0e66d7abb9ab41b7e6ddaf8e222498e4b9c254f828e0ee9d8'
params['pass_ticket'] = 'FpXnhOzYwJ2pazRc2Eq2S4Wpynn7Nitz9WFfNji1POw%3D'
params['x5'] = '0'

headers = {}
headers['Host'] = 'mp.weixin.qq.com'
headers['Accept-Encoding'] ='gzip, deflate'
headers['Connection'] = 'keep-alive'
headers['Proxy-Connection'] = 'keep-alive'
headers['Accept'] = '*/*'
headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12F70 MicroMessenger/6.2.2 NetType/WIFI Language/zh_CN'
headers['refer'] = 'https://mp.weixin.qq.com/s?__biz=MzA4MjA0OTEwMQ==&mid=221566822&idx=1&sn=24843dabf723b6a41e995eb1adfb2453&key=af154fdc40fed003f97328c0686af3643bad92d8140bb4d0e66d7abb9ab41b7e6ddaf8e222498e4b9c254f828e0ee9d8&ascene=1&uin=MjYxMzkyMDM1&devicetype=iPhone+OS8.3&version=16020211&nettype=WIFI&fontScale=100&pass_ticket=XCB%2Fs1iYM1QAXPAeCumA%2FeiNlw9%2F1Ht5chXwCsp3WmE%3D'
headers['Accept-Language'] = 'zh-cn'
headers['X-Requested-With'] = 'XMLHttpRequest'
r = requests.get(wxurl, headers = headers, params = params, verify = False, cookies = cookies)
print r.url
print r.status_code
print r.text

# import urllib3
# import certifi
# import urllib3.contrib.pyopenssl
# urllib3.contrib.pyopenssl.inject_into_urllib3()
#
# http = urllib3.PoolManager(
#     cert_reqs='CERT_REQUIRED', # Force certificate check.
#     ca_certs=certifi.where(),  # Path to the Certifi bundle.
# )
# url ='https://mp.weixin.qq.com/mp/getappmsgext?__biz=MTAzMDM2MjI4MQ==&mid=214752208&sn=4b9e61065912edd684d74f6210e2a656&idx=1&scene=&title=%E5%AF%BB%E7%A7%A6%E8%AE%B0%EF%BC%9A%E5%80%92%E5%9C%A8%E6%89%8B%E6%9C%AF%E5%AE%A4%E7%9A%84%E9%BA%BB%E9%86%89%E4%B8%93%E5%AE%B6&ct=1435639896&devicetype=iPhone&nbsp;OS8.3&version=&f=json&r=0.40540254418738186&is_need_ad=1&comment_id=0&is_need_reward=0&both_ad=1&reward_uin_count=0&uin=MjYxMzkyMDM1&key=af154fdc40fed003857965fd05898f5b9e61e8f02c07db67ba327f5f5e9f0091f72c120bfe62e1722361c4c75d8d353d&pass_ticket=rYaHn8iqNubS9Sp%252BJrv1p5pvOi9TOAluBWb0ugcsGA8%253D&x5=0'
# r = http.request('GET', url)
# print r.data