import numpy as np

poly_args = []
a_linear = 0
b_linear = 0


def horner(x, args):
    result = 0
    for coefficient in args:
        result = result * x + coefficient
    return result


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


def interp(f, n, a, b, xi):
    interp_nodes_x = np.linspace(a, b, num=n)
    interp_nodes_y = f(interp_nodes_x)
    yi = np.zeros(xi.size)

    for i in range(xi.size):
        yi[i] = lagrange_interp(interp_nodes_x, interp_nodes_y, xi[i])
    return xi, yi


def simpson(f, a, b, tol):
    n = 2
    dx = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = interp(f, n, a, b, x)
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    err = np.inf
    while err > tol:
        n *= 2
        dx = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = f(x)
        S_new = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
        err = abs(S - S_new)
        S = S_new
    return S
