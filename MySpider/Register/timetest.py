__author__ = 'qyuan'
import datetime
import time
ltime = time.localtime(1507021110)
timeStr=time.strftime("%Y-%m-%d %H:%M:%S", ltime)
print timeStr