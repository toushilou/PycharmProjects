__author__ = 'qyuan'

class Content:
    def __init__(self, forwardConnectEdge, backwardConnectEdge):
        self.forwardConnectEdge = forwardConnectEdge
        self.backwardConnectEdge = backwardConnectEdge

    def toString(self):
        return self.forwardConnectEdge \
               + ',' \
               + self.backwardConnectEdge

    def reverseString(self):
        return self.backwardConnectEdge \
               + ',' \
               + self.forwardConnectEdge