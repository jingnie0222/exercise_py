#!/usr/bin/python
# -*- coding:gbk -*-
'''lambda����Ҳ��������������������û�о�������ơ�lambda����У�ð��ǰ�ǲ����������ж�����ö��Ÿ�����ð���ұߵķ���ֵ��lambda��乹������ʵ��һ����������'''

def make_repeater (n):
    return lambda s : s * n

twice = make_repeater(2)

print twice ('word')
print twice (5)

str = lambda : 'hello'
'''lambda��������һ�������������Դ˴�Ӧ����str�����������str����ӡ���Ǹú������׵�ַ'''
print str()   
print str 
