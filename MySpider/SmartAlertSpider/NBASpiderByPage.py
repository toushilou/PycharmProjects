# coding = utf-8

import requests
from bs4 import BeautifulSoup


url = 'http://nba.hupu.com/'

r = requests.get(url)

s = r.content

# print s.decode('gb2312')

soup = BeautifulSoup(s)
tag = soup.span
print type(tag)
score_list = soup.find_all('span')

count = 0
result = ''

for score in score_list:
    if score.has_attr('class'):
        if score.text.strip() != '':
            if score['class'][0] != 'curTime':
                if count == 3:
                    print result
                    result = ''
                    count = 0
                result += score.text.strip()
                count += 1
        if score['class'][0] == 'left':
            break