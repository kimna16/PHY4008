import numpy as np
import matplotlib.pyplot as pl

f = lambda t, s: np.exp(-2 * t)
h = 0.1
t = np.arange(0, 1 + h, h)
s0 = -0.5

s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h * f(t[i], s[i])

pl.figure(figsize=(12, 8))
pl.plot(t, s, 'bo--', label='Approximate')
pl.plot(t, -0.5 * np.exp(-2 * t), 'g', label='Exact')
pl.title('Approximate and Exact Solution for Simple ODE')
pl.xlabel('t')
pl.ylabel('f(t)')
pl.grid()
pl.legend(loc='lower right')
pl.show()

def rk2a(f, x0, t):
    n = len(t)
    x = np.array([x0] * n)
    for i in range(n - 1):
        h = t[i + 1] - t[i]
        k1 = h * f(x[i], t[i]) / 2.0
        x[i + 1] = x[i] + h * f(x[i] + k1, t[i] + h / 2.0)
    return x