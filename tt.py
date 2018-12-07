#!/usr/bin/python


structured_template = '''
<doc docId="%(docId)s">
%(summary)s
</doc>'''

data = {'docId':'123','summary':'sss'}

def func():
   xml = structured_template % data
   return xml


if __name__ == '__main__':
    res = func()
    print res

