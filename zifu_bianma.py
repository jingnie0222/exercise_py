#!/usr/bin/python
#coding=utf-8
import chardet
#import sys
#reload (sys)
#sys.setdefaultencoding('utf8')

u = '��'
u1 = u.decode('gbk')
#u = unicode('��')
#print chardet.detect(u1) 
print("---%s---" % repr(u1))

s = u1.encode('utf8')
print("after encode utf8: %s" % s)
print chardet.detect(s)

t = s.decode('utf8')
print("after decode utf8: %s" % t)

# �� su��һ��utf-8��ʽ���ֽڴ�
#u  = su.decode("utf-8")
# �� s������Ϊunicode���󣬸���u

#sg = u.encode("gbk")
# �� u������Ϊgbk��ʽ���ֽڴ�������sg

#s2 = unicode("�������", "utf-8")
#s2 = unicode("�����ַ�").encode("utf-8")
#s2 = u"�����ַ�".encode("utf-8")
#print s2

#print unicode("中文")
#print su
# ��ӡsg
