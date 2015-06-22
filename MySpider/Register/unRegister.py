__author__ = 'sweety'

import requests

url = 'http://my.51durian.com/website/center/backNumber'
payload = {'order_code': '100017806', 'noon_code': ''}
cookies = dict(JSESSIONID='91757C72F2601AB5F190176F48990317')
r = requests.post(url, params = payload, cookies = cookies)

print r.text