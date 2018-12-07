#!/usr/bin/python

number = 50
runflag = True

while runflag:

    guess = input('please enter an integer:')

    if guess == number:
        print 'congratulation~~~'
        #break
        runflag = False
    elif guess > number:
        print 'your enter is larger'
    else:
        print 'your enter is little'
else:
    print 'the loop is over'
