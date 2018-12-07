#!/usr/bin/python
#coding:gbk

#smtplib负责发送邮件，email负责构造邮件

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'yinjingjing@sogou-inc.com'
receivers = ['hyesung_love1127@126.com', 'hyesung_love1127@163.com']
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'gbk')
message['From'] = Header("菜鸟教程", 'gbk')
message['To'] =  Header("测试", 'gbk')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'gbk')

try:
    smtpobj = smtplib.SMTP('mail.163.com', 25)
    smtpobj.set_debuglevel(1)
    smtpobj.Sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
