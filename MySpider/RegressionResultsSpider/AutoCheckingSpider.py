__author__ = 'qyuan'

import xml.etree.cElementTree as etree

xmlFile = open('1_CN_BJ_Case_002.ref', 'r')
root = etree.parse('1_CN_BJ_Case_002.ref')
print(root)