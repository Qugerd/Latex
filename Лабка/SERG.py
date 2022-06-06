from math import sin, pi, exp, cos
import matplotlib.pyplot as plt


def f(t):
    return t / (1 - 4 * t**2)


# return sin(t)
def int_cos(t, w):
    return cos(2 * pi * w * t)


def int_sin(t, w):
    return sin(2 * pi * w * t)


def integral(f, x, func, w):
    return (sum([f(i) * func(i, w) * (x[-1] - x[0]) / len(x) for i in x]))


b = 1 /4

h1 = 100
h2 = 2000
a = 0
x = [(i / h1) * (b - a) + a for i in range(h1)]
y = [f(i) for i in x]
m = 2
omega = [i / h2 * m for i in range(h2)]
integral = [[integral(f, x, int_cos, i), integral(f, x, int_sin,
                                                  i)] for i in omega]
plt.plot(omega, [y[0] for y in integral])
plt.plot(omega, [y[1] for y in integral])
# plt.plot(x, y)
# plt.legend(['cos', 'sin'])
plt.show()

# from math import sin, pi, exp, cos
# import matplotlib.pyplot as plt


# def f(t):
#     return exp(- (t * t)) / t


# # return sin(t)
# def int_cos(t, w):
#     return cos(2 * pi * w * t)


# def int_sin(t, w):
#     return sin(2 * pi * w * t)


# def integral(f, x, func, w):
#     return (sum([f(i) * func(i, w) * (x[-1] - x[0]) / len(x) for i in x]))


# b = 1

# h1 = 100
# h2 = 2000
# a = b / h1
# x = [(i / h1) * (b - a) + a for i in range(h1)]
# y = [f(i) for i in x]
# m = 2
# omega = [i / h2 * m for i in range(h2)]
# integral = [[integral(f, x, int_cos, i), integral(f, x, int_sin,i)] for i in omega]
# plt.plot(omega, [y[0] for y in integral])
# plt.plot(omega, [y[1] for y in integral])
# plt.legend(['cos', 'sin'])
# plt.show()