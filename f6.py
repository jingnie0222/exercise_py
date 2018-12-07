#!/usr/bin/python

def PrintMax(a,b):
    ''' The func means return the max value.

    The two values must be integers.'''
    a = int(a)
    b = int(b)
    if a > b:
        return a
    else:
        return b
print PrintMax(1,10)
print PrintMax.__doc__
    
