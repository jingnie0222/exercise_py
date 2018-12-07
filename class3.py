#!/usr/bin/python

class SchoolMember:
    def __init__(self, name, age):
       self.name = name
       self.age = age
       print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
       print 'Name:%s, Age:%d' % (self.name, self.age),

class Teacher (SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
       SchoolMember.tell(self)
       print 'Salary:%d' % self.salary

class Student (SchoolMember):
    def __init__(self, name, age, marks):
       SchoolMember.__init__(self, name, age)
       self.marks = marks
       print '(Initialized Student: %s)' % self.name
  
    def tell(self):
       SchoolMember.tell(self)
       print 'Marks:%d' % self.marks

t = Teacher ('Andy', 30, 10000)
s = Student ('Erci', 20, 90)

t.tell()
s.tell()

print   # print a blank line

members = [t, s]
for i in members:
    i.tell()













