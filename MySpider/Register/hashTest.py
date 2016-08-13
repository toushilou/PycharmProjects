__author__ = 'sweety'
import math

str = '12312332dfasdfadfdaf'
str1 = '1dsasdfqdsfsdfergsdaf'
print str.__hash__() % 1000
print str1.__hash__() % 1000