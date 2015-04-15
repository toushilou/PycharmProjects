#!/usr/bin/python
# Filename: func_global.py

x = 3
print 'Value of x is', x
def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

func()
print 'Value of x is', x
