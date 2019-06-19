import math
import numpy as np 
import matplotlib.pyplot as plt

def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(np.tanh(w2*xn)) - A*(np.tanh(w1*xn))
    return x_n1

def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en

x = math.inf
x2 = -(math.inf)
x_set = []
x2_set = []
B_set = []
for A in np.arange(0, 40, 0.1):
    for i in range(0, 400):
        y = x_n1(x, 5.82, A, 0.2223, 1.487)
        y2 = x_n1(x2, 5.82, A, 0.2223, 1.487)
        # x = error_estim(1,50, x_set[period], x1)
        # Plot the two lines.
        # plt.plot([x, x], [x, y], 'k', lw=1)
        # plt.plot([x, y], [y, y], 'k', lw=1)

        # Plot the positions with increasing
        # opacity.
        # plt.plot([x], [y], 'ok', ms=10, alpha=(i + 1) / n)
        x = y
        x2=y2
    for j in range(0, 100):
        y = x_n1(x, 5.82, A, 0.2223, 1.487)
        y2 = x_n1(x2, 5.82, A, 0.2223, 1.487)
        x = y
        x2 = y2
        x_set.append(x)
        x2_set.append(x2)
        B_set.append(A)

    # plt.show()



plt.scatter(B_set, x_set, s=0.03)
plt.scatter(B_set, x2_set, s=0.03)
plt.show()



x = math.inf
x2 = -(math.inf)
x_set = []
x2_set = []
B_set = []
for B in np.arange(0, 20, 0.1):
    for i in range(0, 400):
        y = x_n1(x, B, 14.52, 0.2223, 1.487)
        y2 = x_n1(x2, B, 14.52, 0.2223, 1.487)
        # Plot the two lines.
        # plt.plot([x, x], [x, y], 'k', lw=1)
        # plt.plot([x, y], [y, y], 'k', lw=1)

        # Plot the positions with increasing
        # opacity.
        # plt.plot([x], [y], 'ok', ms=10, alpha=(i + 1) / n)
        x = y
        x2=y2
    for j in range(0, 100):
        y = x_n1(x, B, 14.52, 0.2223, 1.487)
        y2 = x_n1(x2, B, 14.52, 0.2223, 1.487)
        x = y
        x2 = y2
        x_set.append(x)
        x2_set.append(x2)
        B_set.append(B)

    # plt.show()



plt.scatter(B_set, x_set, s=0.01)
plt.scatter(B_set, x2_set, s=0.01)
plt.show()