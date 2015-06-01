__author__ = 'qyuan'

import lxml.etree  as etree
import PyQt4.QtGui as QtGui

import sys
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

xmlFile = open('1_CN_BJ_Case_002.ref', 'r')
root = etree.fromstring(xmlFile.read())
children = list(root)
for child in children:
    print child.attrib['rule']
    childNode = list(child)
    for node in childNode:
        attributes = node.attrib
        for attrib in attributes:
            print attrib, '==', attributes[attrib]
        print '---------------'
    print '**************'
sys.exit(app.exec_())