import math
import numpy as np 
import matplotlib.pyplot as plt

def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(np.tanh(w2*xn)) - A*(np.tanh(w1*xn))
    return x_n1

def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en


for A in np.arange(0, 40, 5):
    xn = math.inf
    xn2 = -(math.inf)
    xn_set = []
    xn1_set = []
    A_set = []
    for i in range(0,100):
        xn = x_n1(xn, 5.82, A, 1.487, 0.2223)
        xn2 = x_n1(xn2, 5.82, A, 1.487, 0.2223)
    for i in range(0,100):
        xn = x_n1(xn, 5.82, A, 1.487, 0.2223)
        xn2 = x_n1(xn2, 5.82, A, 1.487, 0.2223)
        xn_set.append(xn)
        xn1_set.append(xn2)
        x_axis = np.arange(0,100,1)
    plt.plot(x_axis, xn_set)
    plt.plot(x_axis, xn1_set)
    plt.show()
    
#     xn_set.append(xn)
#     xn1_set.append(xn2)
#     A_set.append(A)
    


# plt.plot(A_set, xn_set)
# plt.plot(A_set, xn1_set)
plt.show()