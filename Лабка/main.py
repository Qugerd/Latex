from math import sin, pi, exp, cos
import matplotlib.pyplot as plt


def f(t):
    return t / (1 - 4 * t**2)

def intelCos(t, w):
    return cos(2 * pi * w * t)


def intelSin(t, w):
    return sin(2 * pi * w * t)


def intel(f, x, func, w):
    return (sum([f(i) * func(i, w) * (x[-1] - x[0]) / len(x) for i in x]))

a = 0
b = 1/4
h1 = 200
h2 = 1000
m = 2
x = [(i / h1) * (b - a) + a for i in range(h1)]
y = [f(i) for i in x]
W = [i / h2 * m for i in range(h2)]
intel = [[intel(f, x, intelCos, i), intel(f, x, intelSin, i)] for i in omega]

# plt.plot(omega, [y[0] for y in integral])
# plt.plot(omega, [y[1] for y in integral])
plt.plot(x, y)
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
# from math import sin, pi
    
# def func(t):
#     return t / (1 - 4 * t**2)

# a = 0
# b = 1 / 4
# h1 = 100
# h2 = 2000


# def trapezoid_rule(func, a, b, nseg):
#     dx = 1.0 * (b - a) / nseg
#     sum = 0.5 * (func(a) + func(b))
#     for i in range(1, nseg):
#         sum += func(a + i * dx)

#     return sum * dx


# s = trapezoid_rule(f, a, b, 10)
# print('\x1b[6;30;42m' + str(s) + '\x1b[0m')























