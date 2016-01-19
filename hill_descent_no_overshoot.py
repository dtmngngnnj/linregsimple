#!/usr/bin/python 

import matplotlib.pyplot as plt

# function (parabola)
def fx(x): 
    return 5 + (x - 10)**2

def is_down(x1, x2): 
    return True if fx(x1)>fx(x2) else False

step=15.0   # increment 
dx=1e-10    # miniscule value to check direction with, and to compare step with
x0=1.0      # start x
x0d=is_down(x0,x0+dx)   # true if from x0 to x0+dx is going downhill

pt_v=[]     # store points in a list, for plotting
pt_v.append( (x0,fx(x0)) )  

count=0
while step>dx:
    # keep dividing step by two until there is no overshoot
    while True:
        x1=x0+step
        x1d=is_down(x1, x1+dx) 
        if x0d==x1d:    # same direction
            break 
        step=step/2.0
    x0=x1
    x0d=x1d
    pt_v.append( (x0,fx(x0)) )
    count+=1

print "Iterations: ", count,"  Result: ", x0

# plot the function 
xf_v=range(0,21)
yf_v=map( fx, xf_v) 

plt.plot(xf_v,yf_v)        # parabola 
plt.plot(*zip(*pt_v))      # hillclimbing line 
plt.scatter(*zip(*pt_v))   # dots that make up the hillclimbing line
plt.show()



