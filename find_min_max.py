#!/usr/bin/python3
#-*-coding=utf8-*-

def find_min_max(data_lst):
    min = data_lst[0]
    max = data_lst[0]
    for i in data_lst:
        if i < min:
            min = i
            break
        if  i > max:
            max = i
    print(min, max)
    
    
data_lst = [-2,2,2,2,2,2,2]
find_min_max(data_lst)
        