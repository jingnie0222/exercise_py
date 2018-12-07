#!/usr/bin/python
# -*- encoding:gbk -*-

'''s[a:b:-2] 步长为负数，两个边界意义反转了，表示从b+1到a,步长-2'''

list = ['a','b','c','d','e','f','g']

print 'item 0 is',list[0]
print 'item 6 is',list[6]
print 'item -1 is',list[-1]
print 'item -2 is',list[-2]

print 'item 0 to 3',list[0:3]
print 'item 0 to 6',list[:]
print 'item 1 to -1',list[1:-1]
print 'item 3 to -3',list[3:-3]
print 'item 3 to -4',list[3:-4]
print 'item 3 to -5',list[3:-5]

string = 'hyesung'
print 'char 1 to 3 is',string[1:3]
print 'char 2 to end is',string[2:]
print 'char 1 to -1 is',string[1:-1]
print 'char start to end is',string[:]
