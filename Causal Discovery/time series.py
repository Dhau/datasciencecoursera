# Create Two Time Series

import numpy as np
import pylab as pl
from fun import *

def f(x):
    return 4*x*(1-x)

def g(x,alpha):
    return alpha*f(x)

X1 = [0.4]
for i in range(5000):
    X1.append(f(X1[i]))

X2 = [0.1]
for i in range(5000):
    X2.append((1-0.3)*f(X2[i])+0.3*g(X1[i],1))
    
t = [i for i in range(5001)]            
pl.plot(t[1000:1100],X1[1000:1100])
pl.plot(t[1000:1100],X2[1000:1100],"--")
pl.xlabel("n")
pl.ylabel("X1 and X2")
pl.show(1)

print T(X1,X2)

alpha = 0
T12=[]
T21=[]

while alpha <= 1:
    X2 = [0.1]
    for i in range(5000):
        X2.append((1-0.3)*f(X2[i])+0.3*g(X1[i],alpha))
    T12.append(abs(T(X1,X2)[0]))
    T21.append(abs(T(X1,X2)[1]))
    alpha += 0.01

pl.plot(np.arange(0,1,0.01),T12,"--")
pl.plot(np.arange(0,1,0.01),T21)
pl.xlabel("alpha")
pl.ylabel("Information flow")
pl.show(2)