#!/usr/bin/python

import os
import time

source = ['/search/yinjingjing/ppp']
target_dir = '/opt/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S') 
comment = raw_input ('Enter your comment:')

if len(comment) == 0:
    target = today + os.sep + now +  '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory %s ' %  today

zip_command = 'zip -qr %s %s' % (target, ''.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to %s' % target
else:
    print 'Backup Failed' 
