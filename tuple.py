#!/usr/bin/python
# -*- coding:gbk -*-
tuple1 = ('a','b','c',1,2,3)
print 'tuple1\'s length is:',len(tuple1)
for item in tuple1:
    print item,

tuple2 = ('A','B','C',tuple1)
print '\ntuple2\'s length is:',len(tuple2)
print 'tuple2 contains:',tuple2
print 'the forth item of tuple2 is:',tuple2[3]
print 'the fifth item of tuple2[3] is:',tuple2[3][4]

#ʹ��Ԫ���ӡ���

age = 29
name ='����'

print '%s\'s age is %d' % (name,age)
