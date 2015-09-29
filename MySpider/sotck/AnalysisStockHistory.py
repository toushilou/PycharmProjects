__author__ = 'sweety'

import tushare as ts
import numpy as np
import pandas as pd
import scipy as sp

f = open('stock_basic', 'r')
fw = open('stock_history', 'w')
count = 0
result = 0
for line in f:
    stockNumber = line[0:6]
    data = ts.get_hist_data(stockNumber)
    for price in data['price_change']:
        if price <= 0:
            count += 1
        else:
            if count > result:
                result = count
            count = 0
    fw.write(stockNumber+','+str(result))
    fw.write('\r\n')
    print 'done for ', stockNumber
    result = 0
    count = 0

f.close()
fw.close()

# data = sp.genfromtxt("./stock_history", delimiter=',')
#
# x = data[:, 0]
# y = data[:, 1]


# print x
# x = x[np.argsort(-x)]
# y = y[np.argsort(-x)]
# print x
# print y



#print data['open']
