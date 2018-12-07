#!/usr/bin/python
#coding=utf-8
import chardet
#import sys
#reload (sys)
#sys.setdefaultencoding('utf8')

u = '汉'
u1 = u.decode('gbk')
#u = unicode('汉')
#print chardet.detect(u1) 
print("---%s---" % repr(u1))

s = u1.encode('utf8')
print("after encode utf8: %s" % s)
print chardet.detect(s)

t = s.decode('utf8')
print("after decode utf8: %s" % t)

# ： su是一个utf-8格式的字节串
#u  = su.decode("utf-8")
# ： s被解码为unicode对象，赋给u

#sg = u.encode("gbk")
# ： u被编码为gbk格式的字节串，赋给sg

#s2 = unicode("人生苦短", "utf-8")
#s2 = unicode("中文字符").encode("utf-8")
#s2 = u"中文字符".encode("utf-8")
#print s2

#print unicode("涓枃")
#print su
# 打印sg
