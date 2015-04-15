#! /usr/bin/env python
#coding=utf-8
import sys
import os
from utils import PropertiesSet


if __name__=='__main__':
    path = sys.path[0] + os.sep + "test.properties"
    print path
    p = PropertiesSet.Properties(path)
    print p.get('name')