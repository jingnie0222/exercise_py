#!/usr/bin/python
#coding:gbk

import MySQLdb

# �����ݿ�����,username=root,password=YES,database_name=yjj
db = MySQLdb.connect("localhost","root","YES","yjj")

# ʹ��cursor()������ȡ�����α� 
cursor = db.cursor()

# ʹ��execute����ִ��SQL���
cursor.execute("SELECT VERSION()")

# ʹ�� fetchone() ������ȡһ�����ݿ⡣
data = cursor.fetchone()
print(data)

# ������ݱ��Ѿ�����ʹ�� execute() ����ɾ����
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# �������ݱ�SQL���
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)

# SQL �������¼
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # ִ��sql���
    cursor.execute(sql)
    # �ύ�����ݿ�ִ��
    db.commit()
except Exception,e:
    # ��������ʱ�ع�   
    db.rollback()
    print e

# SQL ��ѯ���
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > 1000"
try:
    # ִ��SQL���
    cursor.execute(sql)
    # ��ȡ���м�¼�б�
    results = cursor.fetchall()
    for row in results:
       fname = row[0]
       lname = row[1]
       age = row[2]
       sex = row[3]
       income = row[4]
       # ��ӡ���
       print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % (fname, lname, age, sex, income))
except:
    print "Error: unable to fecth data"

# SQL �������
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # ִ��SQL���
    cursor.execute(sql)
    # �ύ�����ݿ�ִ��
    db.commit()
except:
    # ��������ʱ�ع�
    db.rollback()

# SQL ɾ�����
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # ִ��SQL���
    cursor.execute(sql)
    # �ύ�޸�
    db.commit()
except:
    # ��������ʱ�ع�
    db.rollback()

# �ر����ݿ�����
db.close()
