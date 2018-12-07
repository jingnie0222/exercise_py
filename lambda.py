#!/usr/bin/python
# -*- coding:gbk -*-
'''lambda函数也叫匿名函数，即，函数没有具体的名称。lambda语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。lambda语句构建的其实是一个函数对象。'''

def make_repeater (n):
    return lambda s : s * n

twice = make_repeater(2)

print twice ('word')
print twice (5)

str = lambda : 'hello'
'''lambda创建的是一个函数对象，所以此处应该用str（），如果用str，打印的是该函数的首地址'''
print str()   
print str 
