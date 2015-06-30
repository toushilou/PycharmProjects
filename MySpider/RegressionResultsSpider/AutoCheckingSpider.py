__author__ = 'qyuan'


import sys
import os
from Utils.CommonUtil import *
from rules.ContentRules import *
from MainUI import *

app = QtGui.QApplication(sys.argv)
mw = MainWindow()
mw.show()

ignoreList = ['SID', 'SpeedLimit', 'RoadType', 'RoadSubType', 'RoadPriority', 'Tunnel', 'LaneNumber', 'TrafficDirection', 'Gradient', 'TimeZoneIndex', 'IsBoundingEdge']
rgcCondition = []
contentCondition = []


contentRefDict, contentRefP2PDict = generateReportDic('1_CN_BJ_Case_002.ref')
contentOutDict, contentOutP2PDict = generateReportDic('1_CN_BJ_Case_002.out')

count = 0
matchRange = 300
isMatched = False
for k, v in contentOutDict.items():
    reverseKey = getReverseKey(k)
    startEndpoints = ignoreMidPoints(k)
    if contentRefDict.has_key(k):
        refValue = contentRefDict.get(k)
        if not refValue.toString() == v.toString():
            isMatched = fuzzyMatch(refValue.toString() , v.toString(), matchRange)
        else:
            isMatched = True
    elif  contentRefDict.has_key(reverseKey):
        refValue = contentRefDict.get(reverseKey)
        if not refValue.toString() == v.reverseString():
            isMatched =  fuzzyMatch(refValue.toString() , v.toString(), matchRange)
        else:
            isMatched = True
    if not isMatched:
        if contentRefP2PDict.has_key(startEndpoints):
            originalPoints = contentRefP2PDict.get(startEndpoints)
            refValue = contentRefDict.get(originalPoints)
            isMatched = (refValue.toString() == v.toString())
    if not isMatched:
        print 'Error for key ', k
        print 'The ref is ', refValue.toString()
        print 'The out is ', v.toString()
        count += 1
    else:
        isMatched = False

print 'the mismach result is ', count
sys.exit(app.exec_())