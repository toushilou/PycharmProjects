__author__ = 'qyuan'

import lxml.etree  as etree
import PyQt4.QtGui as QtGui

import sys
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

ignoreList = ['SID', 'SpeedLimit', 'RoadType', 'RoadSubType', 'RoadPriority', 'Tunnel', 'LaneNumber', 'TrafficDirection', 'Gradient', 'TimeZoneIndex', 'IsBoundingEdge']
rgcCondition = []
contentCondition = []
#guidanceCondition = []

xmlFile = open('1_CN_BJ_Case_002.ref', 'r')
root = etree.fromstring(xmlFile.read())
children = list(root)
for child in children:
    print child.attrib['rule']
    childNode = list(child)
    for node in childNode:
        attributes = node.attrib
        for attrib in attributes:
            if attributes[attrib] not in ignoreList:
                print attrib, '==', attributes[attrib]

            else:
                break
        print '---------------'
    print '**************'
sys.exit(app.exec_())