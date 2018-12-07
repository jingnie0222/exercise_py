#!/usr/bin/python
#coding:gbk

import socket

s = socket.socket()          # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
print(host)
port = 12345                 # 设置端口
s.bind((host, port))         # 绑定端口

s.listen(5)                  # 等待客户端连接

while True:
    c,addr = s.accept()      # 建立客户端连接
    print(addr,c)
    c.send('欢迎访问菜鸟教程！')
    c.close()

