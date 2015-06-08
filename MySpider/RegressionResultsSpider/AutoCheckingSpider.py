__author__ = 'qyuan'

import lxml.etree  as etree
import PyQt4.QtGui as QtGui
from Datatypes import Content

import sys
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

ignoreList = ['SID', 'SpeedLimit', 'RoadType', 'RoadSubType', 'RoadPriority', 'Tunnel', 'LaneNumber', 'TrafficDirection', 'Gradient', 'TimeZoneIndex', 'IsBoundingEdge']
rgcCondition = []
contentCondition = []
contentDict = {}
#guidanceCondition = []
forwardConnectEdge, backwardConnectEdge, edgePoint = '', '', ''
xmlFile = open('1_CN_BJ_Case_002.ref', 'r')
root = etree.fromstring(xmlFile.read())
children = list(root)
for child in children:
    childNode = list(child)
    for node in childNode:
        attributes = node.attrib
        nodeName = attributes['name']
        if nodeName == 'ForwardConnectEdge':
            forwardConnectEdge = attributes['value']
        elif nodeName == 'BackwardConnectEdge':
            backwardConnectEdge = attributes['value']
        elif nodeName == 'EdgePoint':
            edgePoint = attributes['value']
    contentDict[edgePoint] = Content.Content(forwardConnectEdge, backwardConnectEdge, edgePoint)

for k, v in contentDict.items():
    print k, ' == ', v.toString()
sys.exit(app.exec_())