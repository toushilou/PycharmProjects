__author__ = 'qyuan'
import lxml.etree  as etree
# import sys
# sys.path.append("..")
from Datatypes import Content
from Datatypes import ContentDict
from rules.ContentRules import *

def generateReportDic(filePath):
    contentDict = {}
    P2PPointsindexDict = {}
    #guidanceCondition = []
    xmlFile = open(filePath, 'r')
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
        contentDict[edgePoint] = Content.Content(forwardConnectEdge, backwardConnectEdge)
        P2PPointsindexDict[ignoreMidPoints(edgePoint)] = edgePoint

    return contentDict, P2PPointsindexDict

def getReverseKey(key):
    edgeArray = key.split(',')
    latArray = edgeArray[0::2]
    lonArray = edgeArray[1::2]
    reverseArray = zip(latArray[::-1], lonArray[::-1])
    reverseKey = ''
    for temp in reverseArray:
        if not reverseKey == '':
            reverseKey += ','
        reverseKey += ','.join(temp)
    return reverseKey