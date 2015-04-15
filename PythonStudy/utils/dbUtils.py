#! /usr/bin/env python
#coding=utf-8
import sys
import os
import PropertiesSet


if __name__=='__main__':
    path = sys.path[0] + os.sep + 'config.properties'
    print path
    p = PropertiesSet.Properties(path)
    print p.get('host')
    print type(type(p.get('host')))