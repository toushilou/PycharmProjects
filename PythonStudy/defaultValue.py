#! /usr/bin/env python
#coding=utf-8
def func(a, b=5, c=10):
    """this is the docString
    
    123123123"""
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c=24)
func(c=50, a=100)
print func.__doc__