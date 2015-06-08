__author__ = 'qyuan'

class Content:
    def __init__(self, forwardConnectEdge, backwardConnectEdge, edgePoint):
        self.forwardConnectEdge = forwardConnectEdge
        self.backwardConnectEdge = backwardConnectEdge
        self.edgePoint = edgePoint

    def toString(self):
        return 'forwardConnectEdge == ' \
               + self.forwardConnectEdge \
               + 'backwardConnectEdge == ' \
               + self.backwardConnectEdge \
               + 'edgePoint == ' \
               + self.edgePoint