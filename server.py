#!/usr/bin/python
#coding:gbk

import socket

s = socket.socket()          # ���� socket ����
host = socket.gethostname()  # ��ȡ����������
print(host)
port = 12345                 # ���ö˿�
s.bind((host, port))         # �󶨶˿�

s.listen(5)                  # �ȴ��ͻ�������

while True:
    c,addr = s.accept()      # �����ͻ�������
    print(addr,c)
    c.send('��ӭ���ʲ���̳̣�')
    c.close()

