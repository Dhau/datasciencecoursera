import numpy as np
import xlrd

fname = "ww.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname

nrows = sh.nrows
ncols = sh.ncols

X1 = sh.col_values(0)
X2 = sh.col_values(1)

print len(X1), len(X2)

C1 = X1[832:1214]
C2 = X2[832:1214]

C11 = np.cov(C1,C1)[0][0]
C12 = np.cov(C1,C2)[0][1]
C21 = np.cov(C2,C1)[0][1]
C22 = np.cov(C2,C2)[0][0]
C1d1 = np.cov(C1,np.diff(X1)[832:1214])[0][1]
C1d2 = np.cov(C1,np.diff(X2)[832:1214])[0][1]
C2d1 = np.cov(C2,np.diff(X1)[832:1214])[0][1]
C2d2 = np.cov(C2,np.diff(X2)[832:1214])[0][1]

T21 = (C11*C12*C2d1-C12*C12*C1d1)/(C11*C11*C22-C11*C12*C12)
T12 = (C22*C21*C1d2-C21*C21*C2d2)/(C22*C22*C11-C22*C21*C21)

print T21,T12


