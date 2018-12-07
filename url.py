#!/usr/bin/python
# -*- encoding:utf8 -*-

import urllib2
import urllib

def getHtml (url):
   request = urllib2.Request(url)
   response = urllib2.urlopen(request)
   return response.read()

html = getHtml("https://10.134.58.87")
#print html

def getPostHtml (url):
   queryString = "中文"
   #querySring_encode = queryString.encode('utf8')   
   value = {"query":queryString}
   data = urllib.urlencode(value)
   print data   
   request = urllib2.Request(url,data)
   response = urllib2.urlopen(request)
   return response.read()

html = getPostHtml("https://10.134.58.87/web?ie=utf8&")
print html
