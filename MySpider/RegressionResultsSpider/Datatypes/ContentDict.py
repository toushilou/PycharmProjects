__author__ = 'qyuan'

class ContentDict(dict):
    def __init__(self):
        dict.__init__(self)
    def get(self, k):
        v = dict.get(self, k)
        if v == None:
            print 'can\'t find'


d = ContentDict()
d.get(123)