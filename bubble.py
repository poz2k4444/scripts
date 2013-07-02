#!/usr/bin/env python

x = [2,5,8,23,87,0,4,67,9,2,5,8,0,2,54,65,7375]

def bubble(x):
    out = True
    while out:
        out = False
        for i in range(0,len(x)-1):
            if x[i] > x[i+1]:
                out = True
                x[i], x[i+1] = x[i+1], x[i]
    print x


bubble(x)
