#!/usr/bin/pathon
# -*- encoding:gbk -*-
import urllib
import urllib2
from bs4 import BeautifulSoup 

def getPage (url):
   request = urllib2.Request(url)
   response = urllib2.urlopen(request)
   return response.read()

#html = getPage("http://op.sogou-inc.com/magic/?mt=web&st=zw_norm_on&key=ee44bfea22fdf9e6-b80c581f9561bd5a-0c72790702b3895511f27cc71dd6b588&udb=10.134.58.87:9010&sid=f5a29ddce91b7bf17555b5f836296890")
html = getPage("http://op.sogou-inc.com/magic/?mt=web&st=zw_norm_on&key=http://you.ctrip.com/sight/phuket364/18402.html&sid=f5a29ddce91b7bf17555b5f836296890")
#html = getPage("http://op.sogou-inc.com/magic/?mt=web&st=zw_norm_on&key=http://you.ctrip.com/sight/phuket364/18402.html")
#print html

'''
soup = BeautifulSoup(html, "lxml")
#soup = BeautifulSoup(html,fromEncoding="gb18030")     # print Chinese characters incorrectly
print soup.original_encoding
#print soup.prettify('gbk')       # print Chinese characters correctly

content=soup.select('div[class="content"]') 
#print 'content:', content 

for i in content:
    print i.encode('gbk')
'''


f = file('tmp', 'w')
f.write(html)
f.close()

f = open('tmp', 'r')
resultlines = []

for oneline in f:
    oneline = oneline.strip()
    oneline = oneline.strip('\n')
    oneline = oneline.strip('\r')
    resultlines.append(oneline)

for i in resultlines:
    print i


