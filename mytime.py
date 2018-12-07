#!/usr/bin/python

import datetime

today = datetime.date.today()
print("today is  %s" % today)

yesdtoday = today - datetime.timedelta(days=1)
print("yesdtoday is  %s" % yesdtoday)

tomorrow = today + datetime.timedelta(days=1)
print("tomorrow is  %s" % tomorrow)

now = datetime.datetime.now()
print("now is  %s" % now)
