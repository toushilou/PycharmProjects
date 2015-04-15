__author__ = 'qyuan'
# coding=utf-8
import requests
import csv

r = requests.get('http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=25&c=2010&d=09&e=8&f=2010&g=d')
reader = csv.reader(file('106.csv', 'r+'))
for line in reader:
    print line

print r._content