import numpy as np

poly_args = []
a_linear = 0
b_linear = 0
exponent_base = 0


def horner(x, args):
    result = 0
    for coefficient in args:
        result = result * x + coefficient
    return result


def exponent(x):
    return exponent_base ** x


def polynomial(x):
    return horner(x, poly_args)


def linear(x):
    return a_linear * x + b_linear


def nested_function(f1, x, f2=None, f3=None):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))


def simpson(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    S = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S


def gauss_chebyshev(f, n):
    x, w = np.polynomial.chebyshev.chebgauss(n)
    return sum(w * f(x))


def chebyshev_nodes(n):
    # Define the Chebyshev nodes
    x = np.zeros(n)
    for i in range(1, n + 1):
        x[i-1] = np.cos(np.pi * (2 * i - 1) / (2 * n))
    return x


def chebyshev_coefficients(f1, f2, f3, n):
    # Chebyshev nodes
    x = chebyshev_nodes(n)

    # function at the Chebyshev nodes
    y = nested_function(f1, x, f2, f3)

    # Chebyshev coefficients
    c = np.zeros(n)
    for k in range(n):
        c[k] = np.sum(y * np.cos(k * np.arccos(x))) * 2 / n
    c[0] = c[0] / 2
    return c


def chebyshev_approximation(f1, f2, f3, n, a, b):
    # Chebyshev coefficients
    c = chebyshev_coefficients(f1, f2, f3, n)

    x = np.linspace(a, b, 1000)
    p = np.zeros(x.size)
    # Chebyshev polynomial approximation of f
    for i in range(x.size):
        for k in range(n):
            p[i] += c[k] * np.cos(k * np.arccos(x[i]))
    return p, x
