import numpy as np
import netCDF4 as nc
import pylab as pl

fname1 = "Fengshen"
fname2 = "Fungwong"
tc1 = nc.Dataset(str.lower(fname1)+".nc")
tc2 = nc.Dataset(str.lower(fname2)+".nc")
totaltime = len(tc1.variables['varcenter'])
#totaltime = len(tc1.variables['varcenter'])-10

k = 1

T1 = []
T2 = []

while k < 34:
    sym1 = []
    sym2 = []
    i = 0
    j = 0
    #i = 10
    #j = 10
    while i < totaltime:
        sym1.append((tc1.variables['varcenter'][i]-tc1.variables['varmin'][i][10])/(tc1.variables['varcenter'][i]-tc1.variables['varmax'][i][10]))
        i += 1
    
    while j < totaltime:
        sym2.append((tc2.variables['varcenter'][j]-tc2.variables['varmin'][j][k])/(tc2.variables['varcenter'][j]-tc2.variables['varmax'][j][k]))
        j += 1
    
    
    #t = [i for i in range(totaltime)]            
    #pl.plot(t,sym1)
    #pl.xlabel("time")
    #pl.ylabel("sym1")
    #pl.plot(t,sym2,"--")
    #pl.xlabel("time")
    #pl.ylabel("sym2")
    #pl.show(2)
    
    #X1 = tc1.variables['slpcenter'][0:totaltime]
    #X2 = tc2.variables['slpcenter'][0:totaltime]
    
    X1 = sym1
    X2 = sym2
    #X2 = np.random.random(len(sym1))
    
    #C1 = X1[0:totaltime-11]
    #C2 = X2[0:totaltime-11]
    C1 = X1[0:totaltime-1]
    C2 = X2[0:totaltime-1]
    
    C11 = np.cov(C1,C1)[0][0]
    C12 = np.cov(C1,C2)[0][1]
    C21 = np.cov(C2,C1)[0][1]
    C22 = np.cov(C2,C2)[0][0]
    C1d1 = np.cov(C1,np.diff(X1)[0:totaltime-1])[0][1]
    C1d2 = np.cov(C1,np.diff(X2)[0:totaltime-1])[0][1]
    C2d1 = np.cov(C2,np.diff(X1)[0:totaltime-1])[0][1]
    C2d2 = np.cov(C2,np.diff(X2)[0:totaltime-1])[0][1]
    
    T21 = (C11*C12*C2d1-C12*C12*C1d1)/(C11*C11*C22-C11*C12*C12)
    T12 = (C22*C21*C1d2-C21*C21*C2d2)/(C22*C22*C11-C22*C21*C21)
    T2.append(T21)
    T1.append(T12)
    k += 1

print T2,T1

str1 = "from "+fname1+" to "+fname2
str2 = "from "+fname2+" to "+fname1  
t = [i for i in range(33)]            
plot1 = pl.plot(t,T1,label=str1)
plot2 = pl.plot(t,T2,"--",label=str2)
pl.title("Information flow at different r ("+fname1+" & "+fname2+")")
pl.xlabel("r (unit: 18km)")
pl.ylabel("Information flow (unit: nats per unit time)")
pl.legend(loc='upper right')
pl.show()
