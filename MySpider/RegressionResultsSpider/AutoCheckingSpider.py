__author__ = 'qyuan'

import PyQt4.QtGui as QtGui
from Utils.CommonUtil import *

import sys
app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

ignoreList = ['SID', 'SpeedLimit', 'RoadType', 'RoadSubType', 'RoadPriority', 'Tunnel', 'LaneNumber', 'TrafficDirection', 'Gradient', 'TimeZoneIndex', 'IsBoundingEdge']
rgcCondition = []
contentCondition = []

contentRefDict = generateReportDic('1_CN_BJ_Case_002.ref')
contentOutDict = generateReportDic('1_CN_BJ_Case_002.out')
count = 0
for k, v in contentOutDict.items():
    reverseKey = getReverseKey(k)
    if contentRefDict.has_key(k):
        refValue = contentRefDict.get(k)
        if not refValue.toString() == v.toString():
            print 'error for key ', k
            print 'ref is ', refValue.toString()
            print 'out is ', v.toString()
    elif  contentRefDict.has_key(reverseKey):
        refValue = contentRefDict.get(reverseKey)
        if not refValue.toString() == v.reverseString():
            print 'error for reverse key: ', reverseKey
            print 'ref is ', refValue.toString()
            print 'out is ', v.reverseString()
        else:
            print 'reverse is match'
    else:
        print 'no match for key ', k
sys.exit(app.exec_())