#!/usr/bin/env python
a = '********'
b = '**    **'
c = '**      '
d = '      **'

try:
    let = int(raw_input("\nEnter a number from 0 to 9: "))
except(ValueError):
    print "That was not a number!" 
else:
    num= let%10
    if num == 1 :
        print '%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\nNumber 1' %(d,d,d,d,d,d,d,d)
    elif num == 4 :
        print '%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\nNumber 4' %(b,b,b,b,a,d,d,d)
    else:
        print '%s'%(a)
        if num == 7 :
            print '%s\n%s\n%s\n%s\n%s\n%s\n%s\nNumber 7' %(d,d,d,d,d,d,d,d)
        elif num == 0 or num == 8 or num == 9 :
            print '%s\n%s\n%s' % (b,b,b)
            if num == 0:
                print '%s\n%s\n%s\n%s\nNumber 0' % (b,b,b,a)
            elif num == 8 :
                print '%s\n%s\n%s\n%s\nNumber 8' % (a,b,b,a)
            else:
                print '%s\n%s\n%s\n%s\nNumber 9' % (a,d,d,a)
        elif num == 2 or num == 3 :
            print '%s\n%s\n%s\n%s' % (d,d,d,a)
            if num == 2:
                print '%s\n%s\n%s\nNumber 2' % (c,c,a)
            else:
                print '%s\n%s\n%s\nNumber 3' % (d,d,a)
        else:
            print '%s\n%s\n%s\n%s' % (c,c,c,a)
            if num == 5:
                print '%s\n%s\n%s\nNumber 5' % (d,d,a)
            else:
                print '%s\n%s\n%s\nNumber 3' % (b,b,a)
    
raw_input("Press enter for exit")
