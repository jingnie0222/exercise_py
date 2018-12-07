#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 gbk 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'gbk')
message['From'] = Header("菜鸟教程", 'gbk')
message['To'] =  Header("测试", 'gbk')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'gbk')


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
