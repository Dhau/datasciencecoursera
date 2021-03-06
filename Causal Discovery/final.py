import numpy as np
import netCDF4 as nc
import pylab as pl

fname1 = "saomai_hgt.nc"
fname2 = "bopha_hgt.nc"
tc1 = nc.Dataset(fname1)
tc2 = nc.Dataset(fname2)
totaltime = len(tc1.variables['slpcenter'])


sym1 = []
sym2 = []
i = 0
j = 0
k = 25

while i < totaltime:
    sym1.append((tc1.variables['slpcenter'][i]-tc1.variables['slpmin'][i][12])/(tc1.variables['slpcenter'][i]-tc1.variables['slpmax'][i][12]))
    i += 1

while j < totaltime:
    sym2.append((tc2.variables['slpcenter'][j]-tc2.variables['slpmin'][j][12])/(tc2.variables['slpcenter'][j]-tc2.variables['slpmax'][j][12]))
    j += 1


t = [i for i in range(totaltime)]            
pl.plot(t,sym1,label = "Saomai")
pl.plot(t,sym2,"--",label = "Bopha")
pl.title("Symmetry when r=10 (Saomai & Bopha)")
pl.xlabel("Time")
pl.ylabel("Symmetry")
pl.legend(loc = 'bottom left')
pl.show(1)

#X1 = tc1.variables['slpcenter'][0:totaltime]
#X2 = tc2.variables['slpcenter'][0:totaltime]

X1 = sym1
X2 = sym2


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

print "T2->1", round(T21,3), "T1->2", round(T12,3)