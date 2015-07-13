__author__ = 'qyuan'

def initPropers(filePath):
    properties = {}
    f = open(filePath, 'r')
    for line in f:
        if line.strip()[0] != '#':
            array = line.split('=')
            if len(array) != 2:
                continue
            else:
                properties[array[0]] = array[1]
    return properties