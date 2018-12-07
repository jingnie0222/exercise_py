#!/usr/bin/python

def func():
    global x
    print 'x is',x
    x=10
    print 'local x is',x

x = 50
func()
print 'extern x is',x


