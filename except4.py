#!/usr/bin/python

try:
    x = input('x:')
    y = input('y:')
    print x/y
#except (ZeroDivisionError, TypeError), e:
except Exception,e:
    print e
    print 'Invalid input'
