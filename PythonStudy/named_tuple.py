#! /usr/bin/env python
#coding=utf-8
from collections import namedtuple

Person = namedtuple('Person', '1 2 3', rename=True)
data = {"name": "John Smith", "hometown": {"name": "New York", "addr": {"firstline" : "5th", "lastline" : "queen"}}}
p = Person('yuanquan','31','male')

def _json_object_hook(d):
    
    for k,v in d.items():
        if isinstance(v, dict):
            d[k] = _json_object_hook(v)

    return namedtuple('X', d.keys())(*d.values())
    
print _json_object_hook(data).hometown.addr.firstline
