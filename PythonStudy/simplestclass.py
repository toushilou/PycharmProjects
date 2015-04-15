#!/usr/bin/python
# Filename: simplestclass.py

class Person:
    def __init__(self, name):
        self.name = name
    
    def sayHi(self,name):
        print 'Hello, my name is', name

p = Person('Swaroop')
p.sayHi('yuanquan')


