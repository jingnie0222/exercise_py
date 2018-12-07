#!/usr/bin/python

class Person:
    pass

p = Person()
print p

class Say:
    def sayhi(self):
        print 'hi~~~'

Say().sayhi()
s = Say()
s.sayhi()

class Person2:
    def __init__(self,name):
        self.name  = name
    def sayhi(self):
        print '%s say hi!!!' % self.name


p1 = Person2('hyesung')
p1.sayhi()

Person2('eric').sayhi()
