#!/usr/bin/python
# -*- coding:gbk -*-

'''由于在args变量前有*前缀 ，所有多余的函数参数都会作为一个元组存储在args中 。如果使用的是**前缀 ，多余的参数则会被认为是一个字典的健/值对.对于def func(*args):，*args表示把传进来的位置参数存储在tuple（元组）args里面。例如，调用func(1, 2, 3) ，args就表示(1, 2, 3)这个元组.对于def func(**args):，**args表示把参数作为字典的健-值对存储在dict（字典）args里面。例如，调用func(a='I', b='am', c='wcdj') ，args就表示{'a':'I', 'b':'am', 'c':'wcdj'}这个字典.'''
def powersum (power, *args):
    total = 0
    for i in args:
        total += pow (i, power)
    return total

print powersum(2, 3, 4)

print powersum(2, 10)


def findad (username, **args):
    print "hi, %s" % username
    for name, email in args.items():
       print 'please contact %s ,%s\'s email is %s' % (name, name, email)

findad('jingnie', hyesung = 'hyesung_mail', eric = 'eric_mail', junjin = 'junjin_mail')
       
