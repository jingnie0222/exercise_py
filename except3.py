#!/usr/bin/python

import time

try:
    f = file('1.txt', 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
           break
        time.sleep(2)
        print line
finally:
    f.close()
    print 'Cleaning up...closed the file'
