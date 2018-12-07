#!/usr/bin/python3
#-*-coding=utf8-*-
from functools import reduce
import math

#Map

def f(x):
    return x*x

L = [1,2,3,4,5]
res = map(f,L)

print(list(res))


#Reduce

def add(x,y):
    return x + y

data = reduce(add, L)
print(data)

#Str into int

def fn(x,y):
    return x *10 + y

def char2num(s):
    digits = {'0':0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

data = reduce(fn, map(char2num, '13579'))
print(data)
print(type(data))

#Normalize name

name = ['adam', 'LISA', 'barT']

def normalize(name):
    return name.capitalize()

print(list(map(normalize, name)))    


#Reduce multiple

def prod(x,y):
    return x * y

print(reduce(prod, L))

#Sorted

L = [9, -5, 6, 50, -30]

dict = {}

for i in L:
    dict[i] = abs(i)

print(sorted(dict.values()))





