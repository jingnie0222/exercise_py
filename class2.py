#!/usr/bin/python
# -*-coding:gbk-*-
'''ע�͵��Ĳ��ֻᱨNoneType��ԭ����Python����globals()����ֵ��key˳�������գ����Ȼ���person���ٻ���andy������population����������ڻ���person���Ѿ��������ˣ����Ի���andy��ʱ��ᱨ��'''
class Person:

    population = 0   # ���е�ʵ��������˱�������������Ϊÿ��ʵ������

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

