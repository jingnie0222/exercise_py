#!/usr/bin/python
#-*-coding:gbk-*-

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#storage = {}
#init(storage)
#for key,value in storage.items():
    #print "%s:%s" % (key, value)

def lookup(data,lable,name):
    print 'Get name %s by %s' % (data[lable].get(name),lable)

#def store(data, fullname):
#    names = fullname.split()
#    if len(names) == 2: names.insert(1, '')
#    lables = 'first', 'middle', 'last'
#    for lable,name in zip(lables, names):
#        people = lookup(data,lable,name)
#    if people:
#        people.append(fullname);
#    else:
#        data[lable][name] = fullname

def store(data, *fullnames):       #实现多个名字同时存储
    for fullname in fullnames:
       names = fullname.split()
       if len(names) == 2: names.insert(1, '')
       lables = 'first', 'middle', 'last'
       for lable,name in zip(lables, names):
          people = lookup(data,lable,name)
       if people:
          people.append(fullname);
       else:
          data[lable][name] = fullname

Mynames = {}
init(Mynames)
store(Mynames, 'yin jing jing', 'xiao jia', 'xiao wang', 'lao li', 'Luke Skywalker', 'Anakin Skywalker')
for key,value in Mynames.items():
    print "%s:%s" % (key, value)
#lookup(Mynames, 'last', 'jing')

