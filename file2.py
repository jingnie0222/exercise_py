#!/usr/bin/python

#import pickle as p
import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = file('shoplistfile', 'w')
#p.dump(shoplist, f)
pickle.dump(shoplist, f)
f.close()

del shoplist

f = file('shoplistfile', 'r')
#storelist = p.load(f)
storelist = pickle.load(f)
print storelist
f.close()
