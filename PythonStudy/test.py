#! /usr/bin/env python
#coding=utf-8
str = r"new lines are indicated by \n"
print(str)
t = lambda x : x**20
print t(4)
for i in range(1, 5, 3):
    print i
else:
    print 'The for loop is over'

while True:
    s = raw_input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    if s == 1
        print 'Input is of sufficient length'
    # Do other kinds of processing here...
