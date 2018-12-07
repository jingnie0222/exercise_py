#!/usr/bin/python
# -*-coding:gbk-*-
'''注释掉的部分会报NoneType错。原因是Python根据globals()这个字典的key顺序来回收，会先回收person，再回收andy。由于population是类变量，在回收person后已经不存在了，所以回收andy的时候会报错。'''
class Person:

    population = 0   # 所有的实例都共享此变量，即不单独为每个实例分配

    def  __init__(self,name):
        self.name = name
        print '%s is coming' % self.name
        Person.population += 1
 
    def __del__(self):
        print '%s is leaving' % self.name
        #Person.population -= 1
        self.__class__.population -= 1

        #if Person.population == 0:
        if self.__class__.population == 0:
            print 'I am the last one.'
        else:
            #print 'There are still %d people left.' % Person.population
            print 'There are still %d people left.' % self.__class__.population

    def sayHi(self):
        print 'hi, my name is %s' % self.name

    def howMany(self):
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here' % Person.population

hyesung = Person('hyesung')
hyesung.sayHi()
hyesung.howMany()

andy = Person('andy')
andy.sayHi()
andy.howMany()

