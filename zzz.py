#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # �����ʼ���������Ϊ���QQ���������������

# ������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� gbk ���ñ���
message = MIMEText('Python �ʼ����Ͳ���...', 'plain', 'gbk')
message['From'] = Header("����̳�", 'gbk')
message['To'] =  Header("����", 'gbk')

subject = 'Python SMTP �ʼ�����'
message['Subject'] = Header(subject, 'gbk')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "�ʼ����ͳɹ�"
except smtplib.SMTPException:
    print "Error: �޷������ʼ�"
