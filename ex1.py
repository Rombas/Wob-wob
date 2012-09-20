#!/usr/bin/env python
try:
    year = float(raw_input("\nEnter current year: "))
except(ValueError):
    print "That was not a number!" 
else:
    if year%400 == 0:
        print "It's leap year!"
    elif year%100 == 0:
        print "It's not leap year!"
    elif year%4 == 0:
        print "It's leap year!"
    else:
        print "It's not leap year!"

raw_input ("Press enter for exit.")
        
