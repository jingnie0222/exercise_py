#!/usr/bin/python
# -*- coding:gbk -*-

'''������args����ǰ��*ǰ׺ �����ж���ĺ�������������Ϊһ��Ԫ��洢��args�� �����ʹ�õ���**ǰ׺ ������Ĳ�����ᱻ��Ϊ��һ���ֵ�Ľ�/ֵ��.����def func(*args):��*args��ʾ�Ѵ�������λ�ò����洢��tuple��Ԫ�飩args���档���磬����func(1, 2, 3) ��args�ͱ�ʾ(1, 2, 3)���Ԫ��.����def func(**args):��**args��ʾ�Ѳ�����Ϊ�ֵ�Ľ�-ֵ�Դ洢��dict���ֵ䣩args���档���磬����func(a='I', b='am', c='wcdj') ��args�ͱ�ʾ{'a':'I', 'b':'am', 'c':'wcdj'}����ֵ�.'''
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
       
