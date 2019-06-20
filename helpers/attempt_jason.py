import math
import numpy as np
import matplotlib.pyplot as plt

def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(math.tanh(w1*xn)) - A*(math.tanh(w2*xn))
    return x_n1

#def x_n1(xn,A):
#    x_n1 = (xn-xn**2) * A
#    return x_n1

def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en

def gnorm(A, An, B, Bn):
    Adiff = ((A/An) -1)* np.sign((A/An) - 1)
    Bdiff = ((B/Bn) -1)* np.sign((B/Bn) - 1)
    gnorm = Adiff - Bdiff
    return gnorm

def output(An, A, B, Bn, M, w3, error_estim, z):
    output = (1.1- (gnorm) * np.tansig(w3 * error_estim))
    return output
    
#xset=[]
#xout=[]
#for x in np.arange(-20,20,0.1):
#    xset.append(x)
#    xout.append(x_n1(x,16.5,5.82,1.487,0.2223))
    
Aset = []
xset=[]
for A in np.arange(1,40,0.1):
    xn = -0.1
    #transient
    for i in range(0,1500,1):
        xnew = x_n1(xn,5.82,A,1.487,0.2223)
        #xnew = x_n1(xn,A)
        xn = xnew
#    print(xn)
    for i in range(0,1000,1):
        xnew = x_n1(xn,5.82,A,1.487,0.2223)
        #xnew = x_n1(xn,A)
        xn = xnew
        xset.append(xn)
        Aset.append(A)
        
for A in np.arange(1,40,0.1):
    xn = 0.1
    #transient
    for i in range(0,1500,1):
        xnew = x_n1(xn,5.82,A,1.487,0.2223)
        #xnew = x_n1(xn,A)
        xn = xnew
#    print(xn)
    for i in range(0,1000,1):
        xnew = x_n1(xn,5.82,A,1.487,0.2223)
        #xnew = x_n1(xn,A)
        xn = xnew
        xset.append(xn)
        Aset.append(A)

plt.figure()
plt.plot(Aset,xset,"bo",markersize=0.01)
plt.show()