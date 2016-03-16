import numpy as np
import xlrd

typhoon = ["201211","201210","201119","201118","201008","201007","200920",
"200919","200820","200819","200724","200723","200713","200712","200610",
"200608","200512","200511","200408","200407","200214","200212"]

fname = "Typhoon_2.xlsx"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)

i = 0

while i <= (len(typhoon)-2):
    try:
        sh1 = bk.sheet_by_name(typhoon[i])
    except:
        print "no sheet in %s named Sheet1" % fname   
    try:
        sh2 = bk.sheet_by_name(typhoon[i+2])
    except:
        print "no sheet in %s named Sheet1" % fname    
    
    X1 = sh1.col_values(9)
    X2 = sh2.col_values(9)
    
    C1 = X1[0:len(X1)-3]
    C2 = X2[0:len(X1)-3]
    
    C11 = np.cov(C1,C1)[0][0]
    C12 = np.cov(C1,C2)[0][1]
    C21 = np.cov(C2,C1)[0][1]
    C22 = np.cov(C2,C2)[0][0]
    C1d1 = np.cov(C1,np.diff(X1)[0:len(X1)-3])[0][1]
    C1d2 = np.cov(C1,np.diff(X2)[0:len(X1)-3])[0][1]
    C2d1 = np.cov(C2,np.diff(X1)[0:len(X1)-3])[0][1]
    C2d2 = np.cov(C2,np.diff(X2)[0:len(X1)-3])[0][1]
    
    T21 = (C11*C12*C2d1-C12*C12*C1d1)/(C11*C11*C22-C11*C12*C12)
    T12 = (C22*C21*C1d2-C21*C21*C2d2)/(C22*C22*C11-C22*C21*C21)
    
    print typhoon[i], typhoon[i+1], "T2->1", round(T21,3), "T1->2", round(T12,3)
    
    i += 1
