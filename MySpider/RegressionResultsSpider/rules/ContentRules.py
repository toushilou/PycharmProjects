__author__ = 'qyuan'

def ignoreMidPoints(edgePoints):

    pointsArray = edgePoints.split(',')
    newEdgePoints = pointsArray[0] + ',' + pointsArray[1] + ',' + pointsArray[-2] + ',' + pointsArray[-1]
    return newEdgePoints

def fuzzyMatch(refEdge, outEdge, range):

    return True

if __name__ == '__main__':
    print ignoreMidPoints('3992534,11641429,3992627,11641434,3992639,11641432,3992646,11641426')
