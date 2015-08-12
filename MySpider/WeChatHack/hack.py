__author__ = 'qyuan'
# coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

url = 'http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FPiajxSqBRaELj042tUfsS4IUv3wibNLH18vhib0YtmmQ1V7zwvXWPrGPdYgia4qkktIKubXP9KFXzQsWBubGbBg7iag%2F0'.replace('%2F','/')
url = url.replace('%3A',':')
print url
cookies = {}
#cookies['pgv_pvi'] = '41287680'
# cookies['rewardsn'] = '607da4e1dd9c4a91046z'
# cookies['pgv_pvid'] = '8194717650'
# cookies['sd_cookie_crttime'] = '1435737207408'
# cookies['sd_userid'] = '96701435737207408'
#cookies['tencentvideo_face'] = 'http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FPiajxSqBRaELj042tUfsS4IUv3wibNLH18vhib0YtmmQ1V7zwvXWPrGPdYgia4qkktIKubXP9KFXzQsWBubGbBg7iag%2F0'
#cookies['tencentvideo_nick'] = '%E8%A2%81%E6%B3%89'
#cookies['tencentvideo_openid'] = 'o-I78jntfAhcGrpPmw722lIj2sbw'
cafile = 'cacert.pem'
wxurl = 'https://mp.weixin.qq.com/mp/getappmsgext'
params = {}
params['__biz'] = 'MzAwNzAwMDgxMw=='
params['mid'] = '220838381'
params['sn'] = '0afd9d655b51e47113c8e548d0dc384e'
params['idx'] = '1'
params['scene'] = '0'
params['title'] = 'MYFM幸运早点名 每天送出105.5块现金 即将开始！'
params['ct'] = '1438653948'
params['devicetype'] = 'iPhone OS8.4'
params['version'] = ''
params['f'] = 'json'
params['r'] = '0.8011194802820683'
params['is_need_ad'] = '1'
params['comment_id'] = '0'
params['is_need_reward'] = '0'
params['both_ad'] = '1'
params['reward_uin_count'] = '0'
params['uin'] = 'MjYxMzkyMDM1'
params['key'] = '0acd51d81cb052bcb37440cba1aa8530534cddcc7a04f63a0fb22aa94de4b7455c067e3639ab00f93ad0a8cb0db8ebc8'
params['pass_ticket'] = 'ChzCc9ScQodJgcYj4VqpmLSUmQUtW9ukIhVXa3%2FtXgM%3D%3D'
params['x5'] = '0'

headers = {}
headers['Host'] = 'mp.weixin.qq.com'
headers['Accept-Encoding'] ='gzip, deflate'
headers['Connection'] = 'keep-alive'
headers['Proxy-Connection'] = 'keep-alive'
headers['Accept'] = '*/*'
headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_4 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H143 MicroMessenger/6.2.3 NetType/WIFI Language/zh_CN'
headers['refer'] = 'https://mp.weixin.qq.com/s?__biz=MjM5ODM0NzM2MA==&mid=209735755&idx=1&sn=ff2e9a89686b058509d3ece79d0c3e7c&scene=0&key=0acd51d81cb052bcab7a09ac9178a5342910aafe1c40daa7caa485ad92724c70cfcc29e088f1749e34452baa0f7d5c29&ascene=1&uin=MjYxMzkyMDM1&devicetype=iPhone+OS8.4&version=16020313&nettype=WIFI&fontScale=100&pass_ticket=ChzCc9ScQodJgcYj4VqpmLSUmQUtW9ukIhVXa3%2FtXgM%3D'
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