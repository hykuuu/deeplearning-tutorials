# -*- coding: utf-8 -*
"""Numerical differentiation: Differentiating into very small differences.
This is an approximate calculation method.
"""


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)


def function(x):
    return 0.01*x**2 + 0.1*x


x = np.arange(0.0, 20.0, 0.1)
y = function(x)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)
plt.show()

print(numerical_diff(function, 5))
print(numerical_diff(function, 10))