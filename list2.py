#!/usr/bin/python

str = "abcd"    #convert str to list
print list(str)

x = [3,5,1,9,6]  # the sort method changes the x list
y = x.sort
print 'x=%s, y=%s' % (x,y)

x = [3,5,1,9,6]  # the sorted method doesn't change the x list
y = sorted(x)   
print 'x=%s, y=%s' % (x,y)
