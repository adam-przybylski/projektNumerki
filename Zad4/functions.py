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


def lagrange_interp(x, y, xi):
    n = len(x)
    li = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                li[i] *= (xi - x[j]) / (x[i] - x[j])
    yi = np.sum(y * li)
    return yi


def weight_function(x):
    return 1 / np.sqrt(1 - x ** 2)


def interp(f1, f2, f3, a, b, xi, ver):
    if len(poly_args) < 5:
        n = 5
    else:
        n = len(poly_args) + 1
    interp_nodes_x = np.linspace(a, b, num=n)
    if ver == 1:
        interp_nodes_y = nested_function(f1, interp_nodes_x, f2, f3) * weight_function(interp_nodes_x)
    else:
        interp_nodes_y = nested_function(f1, interp_nodes_x, f2, f3)
    yi = np.zeros(xi.size)

    for i in range(xi.size):
        yi[i] = lagrange_interp(interp_nodes_x, interp_nodes_y, xi[i])
    return yi


def simpson(f1, f2, f3, a, b, tol):
    n = 2
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = interp(f1, f2, f3, a, b, x, 1)
    # y = f(x) * weight_function(x)
    S = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    err = np.inf
    while err > tol:
        n *= 2
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = interp(f1, f2, f3, a, b, x, 1)
        # y = f(x) * weight_function(x)
        S_new = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
        err = abs(S - S_new)
        S = S_new
    return S


def simpson_with_limit(f1, f2, f3, tol):
    a = 0
    b = 0.5
    temp = simpson(f1, f2, f3, a, b, tol)
    S1 = temp
    while abs(temp) > tol:
        a = b
        b = b + (1 - b) / 2
        temp = simpson(f1, f2, f3, a, b, tol)
        S1 += temp

    a = -0.5
    b = 0
    temp = simpson(f1, f2, f3, a, b, tol)
    S1 += temp
    while abs(temp) > tol:
        b = a
        a = a - (1 + a) / 2
        temp = simpson(f1, f2, f3, a, b, tol)
        S1 += temp

    return S1


def gauss_chebyshev(f1, f2, f3, n):
    x, w = np.polynomial.chebyshev.chebgauss(n)
    y = interp(f1, f2, f3, -1, 1, x, 2)
    return sum(w * y)
