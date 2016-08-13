__author__ = 'sweety'
# coding = utf-8
import requests
import redis
import threading
import time
from bs4 import BeautifulSoup

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            rediscon = redis.Redis(host='42.96.141.125',port=6379,db=0,charset='utf-8',encoding='gbk')
            rediscon.delete('matchList')
            url = 'http://nba.hupu.com/'
            r = requests.get(url)
            s = r.content
            soup = BeautifulSoup(s.decode('gb2312'))
            score_list = soup.find_all('span')

            count = 0
            result = ''

            for score in score_list:
                if score.has_attr('class'):
                    if score.text.strip() != '':
                        if score['class'][0] != 'curTime':
                            if count == 3:
                                print result
                                rediscon.rpush('matchList', result)
                                result = ''
                                count = 0
                            result += score.text.strip()
                            count += 1
                    if score['class'][0] == 'left':
                        break

            time.sleep(60)
myThread = MyThread()

myThread.start()
