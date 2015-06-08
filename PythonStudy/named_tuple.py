#! /usr/bin/env python
#coding=utf-8
from collections import namedtuple

Person = namedtuple('Person', '1 2 3', rename=True)
data = {"name": "Nano_Y", "hometown": {"name": "Shaanxi", "addr": {"firstline" : "Xian", "lastline" : "Gaoxin"}}}
p = Person('yuanquan','31','male')

def _json_object_hook(d):
    
    for k,v in d.items():
        if isinstance(v, dict):
            d[k] = _json_object_hook(v)

    print (d.keys())
    return namedtuple('X', d.keys())(*d.values())
    
print _json_object_hook(data).hometown.addr.firstline

print p._0
