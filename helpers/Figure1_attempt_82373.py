import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import math

# Use LaTeX throughout the figure for consistency
rc('font', **{'family': 'serif', 'serif': ['Computer Modern'], 'size': 16})
rc('text', usetex=True)
# Figure dpi
dpi = 72

def plot_cobweb(f, x0, r, nmax=40):
    """Make a cobweb plot.

    Plot y = f(x; r) and y = x for 0 <= x <= 1, and illustrate the behaviour of
    iterating x = f(x) starting at x = x0. r is a parameter to the function.

    """
    x = np.linspace(-20, 20, 5000)
    fig = plt.figure(figsize=(600/dpi, 450/dpi), dpi=dpi)
    ax = fig.add_subplot(111)

    # Plot y = f(x) and y = x
    ax.plot(x, f(x, r), c='#444444', lw=2)
    ax.plot(x, x, c='#444444', lw=2)

    # Iterate x = f(x) for nmax steps, starting at (x0, 0).
    px, py = np.empty((2,nmax+1,2))
    r_set = []
    px[0], py[0] = x0, 0
    r_set.append([r,r])

    for n in range(1, nmax, 2):
        px[n] = px[n-1]
        py[n] = f(px[n-1], r)
        px[n+1] = py[n]
        py[n+1] = py[n]

        r_set.append([r,r])
        r_set.append([r,r])
    # Plot the path traced out by the iteration.
    ax.plot(px, py, c='b', alpha=0.7)
    # Annotate and tidy the plot.
    ax.minorticks_on()
    ax.grid(which='minor', alpha=0.5)
    ax.grid(which='major', alpha=0.5)
    ax.set_aspect('equal')
    ax.set_xlabel(r)
    ax.set_ylabel(f.latex_label)
    # ax.set_title('$x_0 = {:.1}, r = {:.2}$'.format(x0, r))

    # plt.savefig('cobweb_{:.1}_{:.2}.png', dpi=dpi)
    r_set = np.array(r_set)
    px = np.array(px)

    plt.show()

    return r_set, px


class AnnotatedFunction:
    """A small class representing a mathematical function.

    This class is callable so it acts like a Python function, but it also
    defines a string giving its latex representation.

    """

    def __init__(self, func, latex_label):
        self.func = func
        self.latex_label = latex_label

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

# The logistic map, f(x) = rx(1-x).
func = AnnotatedFunction(lambda x, r: 5.85*(np.tanh(1.487*x)) - r*(np.tanh(0.2223*x)), r'Figure1')

alist = list(range(0,40,5))

r_sset = []
pxx = []

for r in range(0, 40, 2):
    r_set, px = (plot_cobweb(func, math.inf, r))

    r_sset = np.append(r_sset, r_set)
    pxx = np.append(pxx, px)



plt.scatter(r_sset, pxx, s=0.1)
plt.show()


