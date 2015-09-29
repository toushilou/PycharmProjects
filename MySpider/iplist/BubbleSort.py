__author__ = 'qyuan'

def bubleSort():
    a = [23,53,2123,5234,5123,1235,12364,1,532,31236,1,2432,64325,232]
    print a[::-1]
    length = len(a)
    while length > 0:
        for i in range(length - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        length -= 1
    print '1111'
import timeit
import timer
t1 = timeit.Timer('bubleSort()','from __main__ import bubleSort')
print t1.timeit(1)

x=1
L=[]
L.append(x)

def f(x,L=[2]):
        x=2*x
        L.append(x)
        print L,x

f(x)
print "f(x):",L,x

f(x,L)
print "f(x,L):",L,x




