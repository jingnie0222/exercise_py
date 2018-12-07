#!/usr/bin/python

list1 = [3,5,7,1,9]

print 'the list lenght is',len(list1)

print 'the list is:'
for item in list1:
    print item,

print '\nadd an item 2'
list1.append(2)
print 'after add the list is:',list1

list1.sort()
print 'after sort the list is',list1

print 'the third item of the list is:',list1[2]

del list1[0]
print 'delete the first item ,the list is',list1

print 'the count of 9:',list1.count(9)


bag = ['a','b','c','d','e']
for (index,element) in enumerate(bag):
    print (index,element)
