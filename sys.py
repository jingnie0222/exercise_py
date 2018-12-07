#!/usr/bin/python

import sys

def readfile(filename):
    f = file(filename, 'r')
    while True:
       line = f.readline()
       if len(line) == 0:
          break
       print line,
    f.close()


if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'version':
       print 'Version 1.0'
    elif option == 'help':
       print '''Help'''
    else:
       print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
       readfile(filename)
