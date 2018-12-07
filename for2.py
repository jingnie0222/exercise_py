#!/usr/bin/python 

name = ['aaa', 'bbb', 'ccc']
age = [1,2,3]
zip_res = zip(name,age)
print "zip result is:",zip_res

for name,age in zip_res:
    print "%s's old is %d" % (name,age)
