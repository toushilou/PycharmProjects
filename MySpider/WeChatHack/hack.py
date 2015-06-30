__author__ = 'qyuan'
# import requests
# url = 'http%3A%2F%2Fwx.qlogo.cn%2Fmmopen%2FPiajxSqBRaELj042tUfsS4IUv3wibNLH18vhib0YtmmQ1V7zwvXWPrGPdYgia4qkktIKubXP9KFXzQsWBubGbBg7iag%2F0'.replace('%2F','/')
# url = url.replace('%3A',':')
# print url
# cookies = {'pgv_pvi': '41287680', 'pgv_pvid	': '9917116262', 'sd_cookie_crttime':	'1430731556250', 'sd_userid':'26151430731556250', 'tencentvideo_face': url, 'tencentvideo_nick': '%E8%A2%81%E6%B3%89', 'tencentvideo_openid': 'o-I78jntfAhcGrpPmw722lIj2sbw'}
# cafile = 'cacert.pem'
# r = requests.get('https://mp.weixin.qq.com/mp/getappmsgext?__biz=MTAzMDM2MjI4MQ==&mid=214752208&sn=4b9e61065912edd684d74f6210e2a656&idx=1&scene=&title=%E5%AF%BB%E7%A7%A6%E8%AE%B0%EF%BC%9A%E5%80%92%E5%9C%A8%E6%89%8B%E6%9C%AF%E5%AE%A4%E7%9A%84%E9%BA%BB%E9%86%89%E4%B8%93%E5%AE%B6&ct=1435639896&devicetype=iPhone&nbsp;OS8.3&version=&f=json&r=0.40540254418738186&is_need_ad=1&comment_id=0&is_need_reward=0&both_ad=1&reward_uin_count=0&uin=MjYxMzkyMDM1&key=af154fdc40fed003857965fd05898f5b9e61e8f02c07db67ba327f5f5e9f0091f72c120bfe62e1722361c4c75d8d353d&pass_ticket=rYaHn8iqNubS9Sp%252BJrv1p5pvOi9TOAluBWb0ugcsGA8%253D&x5=0', verify=cafile, cookies=cookies)
# print r.text

import urllib3
import certifi
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED', # Force certificate check.
    ca_certs=certifi.where(),  # Path to the Certifi bundle.
)
url ='https://mp.weixin.qq.com/mp/getappmsgext?__biz=MTAzMDM2MjI4MQ==&mid=214752208&sn=4b9e61065912edd684d74f6210e2a656&idx=1&scene=&title=%E5%AF%BB%E7%A7%A6%E8%AE%B0%EF%BC%9A%E5%80%92%E5%9C%A8%E6%89%8B%E6%9C%AF%E5%AE%A4%E7%9A%84%E9%BA%BB%E9%86%89%E4%B8%93%E5%AE%B6&ct=1435639896&devicetype=iPhone&nbsp;OS8.3&version=&f=json&r=0.40540254418738186&is_need_ad=1&comment_id=0&is_need_reward=0&both_ad=1&reward_uin_count=0&uin=MjYxMzkyMDM1&key=af154fdc40fed003857965fd05898f5b9e61e8f02c07db67ba327f5f5e9f0091f72c120bfe62e1722361c4c75d8d353d&pass_ticket=rYaHn8iqNubS9Sp%252BJrv1p5pvOi9TOAluBWb0ugcsGA8%253D&x5=0'
r = http.request('GET', url)
print r.data