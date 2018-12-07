#!/usr/bin/python

class ShortInputException (Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input('Enter something:\n')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print 'There is EOFError'
except ShortInputException, x:
    if isinstance(x, ShortInputException):
        print 'x is an instance of ShortInputException.'    
        print 'ShortInputException: The input was of length %d, was expecting at least %d' % (x.length, x.atleast)

else:
    print 'No exception was raised.'
