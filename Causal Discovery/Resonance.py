import math
import pylab
import numpy
from fun import *


def f(t):
    return numpy.cos(t)

def g(t):
    return t*(numpy.sin(t))/2

X1=[]
X2=[]
dX1 = []
dX2 = []

for i in numpy.arange(0,10,0.00001):
    X1.append(f(i))

for i in numpy.arange(0,10,0.00001):
    X2.append(g(i))

for i in range(len(X1)-1):
    dX1.append((X1[i+1]-X1[i])/0.00001)

for i in range(len(X2)-1):
    dX2.append((X2[i+1]-X2[i])/0.00001)

C1 = X1[0:len(X2)-1]
C2 = X2[0:len(X2)-1]

C11 = np.cov(C1,C1)[0][0]
C12 = np.cov(C1,C2)[0][1]
C21 = np.cov(C2,C1)[0][1]
C22 = np.cov(C2,C2)[0][0]
C1d1 = np.cov(C1,dX1)[0][1]
C1d2 = np.cov(C1,dX2)[0][1]
C2d1 = np.cov(C2,dX1)[0][1]
C2d2 = np.cov(C2,dX2)[0][1]
T21 = (C11*C12*C2d1-C12*C12*C1d1)/(C11*C11*C22-C11*C12*C12)
T12 = (C22*C21*C1d2-C21*C21*C2d2)/(C22*C22*C11-C22*C21*C21)

print T12,T21

x = numpy.arange(0,10,0.1)

pylab.figure(1)
pylab.plot(x, f(x))
pylab.plot(x, g(x))
pylab.xlabel('Distance')
pylab.ylabel('Surface Elevation')
pylab.show()
