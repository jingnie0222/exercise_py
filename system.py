#!/usr/bin/python

import os

print 'os.system  result is %s ' % os.system('sh hello.sh')
print 'os.popen result is %s ' % os.popen('sh hello.sh').read()
