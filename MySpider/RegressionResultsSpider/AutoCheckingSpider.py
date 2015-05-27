__author__ = 'qyuan'

import lxml.etree  as etree

xmlFile = open('1_CN_BJ_Case_002.ref', 'r')
root = etree.fromstring(xmlFile.read())
children = list(root)
for child in children:
    print child.attrib['rule']
    childNode = list(child)
    for node in childNode:
        attributes = node.attrib
        for attrib in attributes:
            print attributes[attrib]
        print '---------------'
    print '**************'
