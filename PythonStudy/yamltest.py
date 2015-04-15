#! /usr/bin/env python
#coding=utf-8
import yaml
f = open('yamltest.yaml')
dataMap = yaml.load(f)
f.close()

# dataMap: 
print dataMap
#print dataMap['treeroot']['branch2']

f = open('newtree.yaml', "w")
yaml.dump(dataMap, f)
f.close()
