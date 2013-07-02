#!/usr/bin/env python

x = [2,5,8,23,87,2340,4,67,9542,2,5,8,0,2,54,65,7375]

def selection(x):
    count = 0
    minV = 0
    while count < len(x):
        #minV = 0
        for i in range (count, len(x)):
            if x[minV] > x[i]:
                minV = i
        x[count], x[minV] = x[minV], x[count]
        count += 1
        print "min value: " + str(minV)
        minV = count
    print x


selection(x)
