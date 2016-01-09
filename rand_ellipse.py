'''
Daniel Kronovet
dbk2123@columbia.edu

Code to draw "randomly" from a zero-mean ellipse.

Approach:
    Fix x,y. There exists a scalar c such that c(x,y) is a solution to
    the ellipse. We find c and scale (x,y).

Parameters:
a (x-axis scaling)
b (y-axis scaling)
alpha (rotation, radians)
'''

import matplotlib.pyplot as plt
import numpy as np


# Parameters
a = 1
b = 1
alpha = 0

def draw_u(n=1):
    mean = [0, 0]
    cov = [[1, 0],
           [0, 1]]
    return np.random.multivariate_normal(mean, cov, n)

def solve_c(u, a=a, b=b, alpha=alpha):
    x, y = u[0], u[1]
    t1 = ((x*np.cos(alpha) + y*np.sin(alpha))**2) / (a**2)
    t2 = ((x*np.sin(alpha) + y*np.cos(alpha))**2) / (b**2)
    return 1 / np.sqrt(t1 + t2)

def scale(u, a=a, b=b, alpha=alpha):
    c = solve_c(u, a, b, alpha)
    z = c*u
    return z

def draw():
    u = draw_u()
    c = solve_c(u)
    z = c*u
    return z

def plot(Z, subplot, alpha):
    '''Plot an array Z of points'''
    x, y = zip(*Z)
    subplot.plot(x, y)
    subplot.set_title(alpha)


def l2_norm(z):
    return np.sqrt(sum([zi**2 for zi in z]))


if __name__ == '__main__':
    import sys

    n = int(sys.argv[1])
    U = draw_u(n)

    f, sub = plt.subplots(2, 2, sharex=True, sharey=True)
    for k, alpha in enumerate([np.pi, np.pi/2, np.pi/4, np.pi/6]):
        Z = [scale(u, a, b, alpha) for u in U]
        i, j = k/2, k%2
        plot(Z, sub[i, j], alpha)

    plt.show()


