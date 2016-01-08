import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]

v1 = 1
v2 = .2
cv = .4

# cv must be <= max(v1, v2) else not psd

cov = [[v1, cv],
       [cv, v2]]

x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()