#!/usr/bin/python

import mymodule
from mymodule import sayhi,version

mymodule.sayhi()
sayhi()

print 'mymodule version is',mymodule.version
print 'mymodule version is',version
