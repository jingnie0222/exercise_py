#!/usr/bin/python
#coding:gbk

#smtplib�������ʼ���email�������ʼ�

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'yinjingjing@sogou-inc.com'
receivers = ['hyesung_love1127@126.com', 'hyesung_love1127@163.com']
# ������������һ��Ϊ�ı����ݣ��ڶ��� plain �����ı���ʽ�������� utf-8 ���ñ���
message = MIMEText('Python �ʼ����Ͳ���...', 'plain', 'gbk')
message['From'] = Header("����̳�", 'gbk')
message['To'] =  Header("����", 'gbk')

subject = 'Python SMTP �ʼ�����'
message['Subject'] = Header(subject, 'gbk')

try:
    smtpobj = smtplib.SMTP('mail.163.com', 25)
    smtpobj.set_debuglevel(1)
    smtpobj.Sendmail(sender, receivers, message.as_string())
    print("�ʼ����ͳɹ�")
except smtplib.SMTPException:
    print("Error: �޷������ʼ�")
