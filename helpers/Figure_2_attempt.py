import math
import numpy as np 
import matplotlib.pyplot as plt

def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(math.tanh(w2*xn)) - A*(math.tanh(w1*xn))
    return x_n1

def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en

xn_set = []
A_set = []
xn = math.inf
for A in np.arange(0, 40, 0.01):

    xn = x_n1(xn, 5.82, A, 1.487, 0.2223)
    xn_set.append(xn)

    A_set.append(A)
    

plt.plot(A_set, xn_set)
plt.show()