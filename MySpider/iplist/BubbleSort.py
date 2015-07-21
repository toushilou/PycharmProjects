__author__ = 'qyuan'

def bubleSort():
    a = [23,53,2123,5234,5123,1235,12364,1,532,31236,1,2432,64325,232]
    length = len(a)
    while length > 0:
        for i in range(length - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        length -= 1
import timeit
import timer
t1 = timeit.Timer('bubleSort()')
print timeit(bubleSort())


