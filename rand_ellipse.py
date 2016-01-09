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
b = 2
alpha = np.pi/3

def draw_u(n=1):
    mean = [0, 0]
    cov = [[1, 0],
           [0, 1]]
    return np.random.multivariate_normal(mean, cov, n)

def solve_c(u, a=a, b=b, alpha=alpha):
    x, y = u[0], u[1]
    t1 = ((x*np.cos(alpha) + y*np.sin(alpha))**2) / (a**2)
    t2 = ((x*np.sin(alpha) - y*np.cos(alpha))**2) / (b**2)
    return 1 / np.sqrt(t1 + t2)

def scale(u, a=a, b=b, alpha=alpha):
    c = solve_c(u, a, b, alpha)
    z = c*u
    return z

def plot(Z):
    '''Plot an array Z of points'''
    x, y = zip(*Z)
    plt.plot(x, y, 'x')
    plt.axis('equal')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.show()

def l2_norm(z):
    return np.sqrt(sum([zi**2 for zi in z]))


if __name__ == '__main__':
    import sys

    n = int(sys.argv[1])
    U = draw_u(n)
    Z = [scale(u) for u in U]
    plot(Z)


