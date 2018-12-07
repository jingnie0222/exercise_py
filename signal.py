#!/usr/bin/python

import sys
import os
import signal
import time

def onsignal_term ( ):
    print 'receive SIGTERM'
    sys.exit()

signal.signal(signal.SIGTERM, onsignal_term)

def onsignal_usr1 ( ):
    print 'receive SIGUSR1'
    sys.exit()

signal.signal(signal.SIGUSR1, onsignal_usr1)

while True:
    print 'My process id is %d' % os.getpid()
    time.sleep(10)
