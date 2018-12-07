#!/usr/bin/python

import sys

print 'the command arguments are:'

for i in sys.argv:
    print i
print '\n\nthe PYTHOBPATH is',sys.path,'\n'
