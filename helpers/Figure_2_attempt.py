import math
import numpy as np 
import matplotlib.pyplot as plt

#Equation 1
def x_n1(xn, B, A, w1, w2):
    x_n1 = B*(np.tanh(w2*xn)) - A*(np.tanh(w1*xn))
    return x_n1

#Equation 2
def error_estim(n1, n2, xn, xp): 
    en = (1/(n2-n1+1))*(abs((xn-xp) - xn))
    return en

#PLotting x as a function of iterations, this was done to produce the bifuration map and produce plots that show the dynamics of x at each value of A/B
x = 0.5
x2 = -0.5
x_set = []
x1_set = []
x2_set = []
B_set = []
color = []
for B in np.arange(0, 20, 0.1):
    x_color = []
    xas = []
    ias = []
    for i in range(0, 10):
        y = x_n1(x, B, 14.47, 0.2223, 1.487)
        y2 = x_n1(x2, B, 14.47, 0.2223, 1.487)
        # Plot the two lines.
        # plt.plot([x, x], [x, y], 'k', lw=1)
        # plt.plot([x, y], [y, y], 'k', lw=1)

        # Plot the positions with increasing
        # opacity.
        # plt.plot([x], [y], 'ok', ms=10, alpha=(i + 1) / n)
        x = y
        x_set.append(x)
        x2=y2
    for j in range(0, 100):
        y = x_n1(x, B, 14.47, 0.2223, 1.487)
        y2 = x_n1(x2, B, 14.47, 0.2223, 1.487)
        x = y
        x2 = y2
        x1_set.append(x)
        x2_set.append(x2)
        B_set.append(B)
        x_color.append(x)
        xas.append(x)
        ias.append(j)
    # plt.scatter(ias, xas, c='r',s=8.9, zorder=2)
    # plt.plot(ias, xas, zorder=1)
    # plt.title('Values x takes as a function of iteration steps with A = %s' %A)
    # plt.ylabel('x')
    # plt.xlabel('k')
    # plt.show()
    color.append(list(set(x_color)))

#Colouring the bifurcation diagram based on density of values x takes at eeach value of A/B
z = []
for aasd in color:
    if len(aasd) < 3:
        for i in range(100):
            z.append(1)
    elif 3<= len(aasd) < 25:
        for i in range(100):
            z.append(2)
    elif 25<= len(aasd) < 101:
        for i in range(100):
            z.append(3)


#Plotting the bifurcation map
plt.rcParams['axes.facecolor'] = 'grey'
plt.scatter(B_set, x1_set, s=0.03, c='b', cmap='Reds')
plt.scatter(B_set, x2_set, s=0.03, c='r', cmap='Reds')
plt.title('Bifurcation map of values of x with changing B')
plt.ylabel('$x_{inf}$')
plt.xlabel('B')
plt.show()


