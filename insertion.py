#!/usr/bin/env python

x = [22346,5,8,23,87,0,4,67,9,542,574,988,530,2,54,65,7375]

def insertion(x):
    y =[]
    count = 1
    if len(y) is 0:
        y.append(x[0])
    while count < len(x):
        position = 0
        out = True
        while out:
            if x[count] <= y[position]:
                y.insert(position, x[count])
                out = False
            elif position is len(y)-1:
                y.append(x[count])
                out = False
            else:
                position +=1
        count +=1
    print x
    print y

insertion(x)
