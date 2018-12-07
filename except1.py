#!/usr/bin/python

import sys

try:
    s = raw_input('please enter someting:\n')
except EOFError:
    print 'There is an EOFError'
    #sys.exit()
except:
    print 'Some error/exception occurred.'

print 'Done'
