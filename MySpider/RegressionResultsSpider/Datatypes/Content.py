__author__ = 'qyuan'

class Content:
    def __init__(self, forwardConnectEdge, backwardConnectEdge):
        self.forwardConnectEdge = forwardConnectEdge
        self.backwardConnectEdge = backwardConnectEdge

    def toString(self):
        return 'forwardConnectEdge == ' \
               + self.forwardConnectEdge \
               + 'backwardConnectEdge == ' \
               + self.backwardConnectEdge

    def reverseString(self):
        return 'forwardConnectEdge == ' \
               + self.backwardConnectEdge \
               + 'backwardConnectEdge == ' \
               + self.forwardConnectEdge