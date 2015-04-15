#! /usr/bin/env python
#coding=utf-8

import json
from collections import namedtuple

class Nested(object):
	"""Nested represents a dumb object, that converts a given dict 
	to internal attributes. There are several ways to map a dict to
	an object.
	
	This one is based on my question at stackoverflow:
	http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
	"""
	
	
	def __init__(self, d={}):
		"""Convert dict to class attributes.
		"""
		
		for a, b in d.items():
			# handle lists and tuples
			if isinstance(b, (list, tuple)):
				setattr(self, a, 
					[Nested(x) if isinstance(x, dict) else x for x in b])
			# the rest
			else:
				setattr(self, a, Nested(b) if isinstance(b, dict) else b)

if __name__ == '__main__':
    d =  {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
    do = Nested(d);
    print do.d[1].foo
    obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    encodedjson = json.dumps(obj)
    print repr(obj)
    print encodedjson
    
    data = '{"name": "John Smith", "hometown": {"name": "New York", "id": [123,456]}}'
    
    # Parse JSON into an object with attributes corresponding to dict keys.
    x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    t = '{"a": 1, "b": {"c": 2}, "d": ["hi", {"foo": "bar"}]}'
    m = json.loads(t)
    
    y = json.loads(t, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    print x.name, x.hometown.name, x.hometown.id[0]
    print y.d[1].foo
