__author__ = 'sweety'

import tushare as ts
import pandas
import scipy as sp

#f = open('stock_basic', 'w')

df = ts.get_stock_basics()
#df.to_csv('stock_basic', encoding='gbk')

