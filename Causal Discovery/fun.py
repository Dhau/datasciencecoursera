import numpy as np
import pylab as pl

def C11(X1):
    C1 = X1[1000:1990]
    return np.cov(C1,C1)[0][0]

def C12(X1,X2):
    C1 = X1[1000:1990]
    C2 = X2[1000:1990]
    return np.cov(C1,C2)[0][1]

def C21(X2,X1):
    C1 = X1[1000:1990]
    C2 = X2[1000:1990]
    return np.cov(C2,C1)[0][1]
    
def C22(X2):
    C2 = X2[1000:1990]
    return np.cov(C2,C2)[0][0]

def C1d1(X1):
    C1 = X1[1000:1990]
    dX1 = np.diff(X1)
    return np.cov(C1,dX1)[0][1]

def C1d2(X1,X2):
    C1 = X1[1000:1990]
    dX2 = np.diff(X2)    
    return np.cov(C1,dX2)[0][1]

def C2d1(X1,X2):
    C2 = X2[1000:1990]
    dX1 = np.diff(X1) 
    return np.cov(C2,dX1)[0][1]

def C2d2(X2):
    C2 = X2[1000:1990]
    dX2 = np.diff(X2)
    return np.cov(C2,dX2)[0][1]

def T21(X1,X2):
    return ((C11(X1)*C12(X1,X2)*C2d1(X2,X1)-C12(X1,X2)*C12(X1,X2)*C1d1(X1))/(C11(X1)*C11(X1)*C22(X2)-C11(X1)*C12(X1,X2)*C12(X1,X2)))

def T12(X1,X2):
    return ((C22(X2)*C12(X1,X2)*C1d2(X1,X2)-C12(X1,X2)*C12(X1,X2)*C2d2(X2))/(C22(X2)*C22(X2)*C11(X1)-C22(X2)*C12(X1,X2)*C12(X1,X2)))

def T(X1,X2):
    C1 = X1[1000:5000]
    C2 = X2[1000:5000]
    C11 = np.cov(C1,C1)[0][0]
    C12 = np.cov(C1,C2)[0][1]
    C21 = np.cov(C2,C1)[0][1]
    C22 = np.cov(C2,C2)[0][0]
    C1d1 = np.cov(C1,np.diff(X1)[1000:5000])[0][1]
    C1d2 = np.cov(C1,np.diff(X2)[1000:5000])[0][1]
    C2d1 = np.cov(C2,np.diff(X1)[1000:5000])[0][1]
    C2d2 = np.cov(C2,np.diff(X2)[1000:5000])[0][1]
    T21 = (C11*C12*C2d1-C12*C12*C1d1)/(C11*C11*C22-C11*C12*C12)
    T12 = (C22*C21*C1d2-C21*C21*C2d2)/(C22*C22*C11-C22*C21*C21)
    return T21,T12

