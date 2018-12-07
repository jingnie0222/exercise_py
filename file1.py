#!/usr/bin/python

poem = '''\
programming is fun
when the work is done
if you wanna make your work also fun:
       use puthon!
'''

f = file('1.txt', 'w')
f.write(poem)
f.close()

f = file('1.txt', 'r')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line,

f.close()
