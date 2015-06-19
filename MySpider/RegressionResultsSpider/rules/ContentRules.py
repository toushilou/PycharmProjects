__author__ = 'qyuan'
import math

def ignoreMidPoints(edgePoints):

    pointsArray = edgePoints.split(',')
    newEdgePoints = pointsArray[0] + ',' + pointsArray[1] + ',' + pointsArray[-2] + ',' + pointsArray[-1]
    return newEdgePoints

def fuzzyMatch(refEdge, outEdge, matchRange):
    refEdge = refEdge.replace('|', ',')
    outEdge = outEdge.replace('|', ',')
    refArray = refEdge.split(',')
    outArray = outEdge.split(',')
    if not len(refArray) == len(outArray):
        return False
    outRefArray = zip(refArray, outArray)

    for item in outRefArray:
        try:
            if math.fabs(int(item[0]) - int(item[1])) > matchRange:
                return False
        except ValueError, e:
            continue
    return True

if __name__ == '__main__':
    print ignoreMidPoints('3992534,11641429,3992627,11641434,3992639,11641432,3992646,11641426')
