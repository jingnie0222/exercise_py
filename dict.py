#!/usr/bin/python
# -*-coding:gbk-*-
dict = {'A':'alibaba','B':'baidu','S':'sogou'}

#默认打印
for key,value in dict.items():   
    print ' %s %s' % (key,value)

print 'dict.iterkeys:',dict.iterkeys()
print 'dict.itervalues:',dict.itervalues()
print 'dict.iteritems:',dict.iteritems()

print "A\'s value is:",dict['A']

dict['T'] = 'tencent'
for (key,value) in dict.items():
    print '%s %s' % (key,value)

del dict['A']
for (key,value) in dict.items():
    print '%s %s' % (key,value)

if 'S' in dict:
    print 'S\'s value is:',dict['S']

input = raw_input('please enter a character:')
if dict.has_key(input):
    print '%s is in the dict' % input
else:
    print '%s is not in the dict' % input
