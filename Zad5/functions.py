import numpy as np

poly_args = []
a_linear = 0
b_linear = 0
exponent_base = 0
f1 = None
f2 = None
f3 = None


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


def nested_function(x):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))


def weight_function(x):
    return 1 / np.sqrt(1 - x ** 2)


def chebyshev_polynomial(x, k):
    return np.cos(k * np.arccos(x))


def simpson(a, b, k, epsilon, version=1):
    n = 2
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    if version == 1:
        y = nested_function(x) * chebyshev_polynomial(x, k) * weight_function(x)
    else:
        y = chebyshev_polynomial(x, k) * chebyshev_polynomial(x, k) * weight_function(x)
    S = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    err = np.inf
    while err > epsilon:
        n *= 2
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        if version == 1:
            y = nested_function(x) * chebyshev_polynomial(x, k) * weight_function(x)
        else:
            y = chebyshev_polynomial(x, k) * chebyshev_polynomial(x, k) * weight_function(x)
        S_new = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
        err = abs(S - S_new)
        S = S_new
    return S


def simpson_with_limit(k, epsilon, version=1):
    a = 0
    b = 0.5
    temp = simpson(a, b, k, epsilon, version)
    S1 = temp
    while abs(temp) > epsilon:
        a = b
        b = b + (1 - b) / 2
        temp = simpson(a, b, k, epsilon, version)
        S1 += temp

    a = -0.5
    b = 0
    temp = simpson(a, b, k, epsilon, version)
    S1 += temp
    while abs(temp) > epsilon:
        b = a
        a = a - (1 + a) / 2
        temp = simpson(a, b, k, epsilon, version)
        S1 += temp

    return S1


def simpson_error(p, x, a, b):
    h = (b - a) / (x.size - 1)
    y = (nested_function(x) - p) ** 2
    S = h / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return S


def chebyshev_nodes(n):
    # Define the Chebyshev nodes
    x = np.zeros(n)
    for i in range(1, n + 1):
        x[i - 1] = np.cos(np.pi * (2 * i - 1) / (2 * n))
    return x


def chebyshev_coefficients(n):
    # Chebyshev nodes
    x = chebyshev_nodes(n)

    # function at the Chebyshev nodes
    y = nested_function(x)

    # Chebyshev coefficients
    c = np.zeros(n)
    for k in range(n):
        c[k] = np.sum(y * np.cos(k * np.arccos(x))) * 2 / n
    c[0] = c[0] / 2
    return c


def chebyshev_coefficients2(n, epsilon):
    # Chebyshev coefficients
    c = np.zeros(n + 1)
    for k in range(n + 1):
        c[k] = simpson_with_limit(k, epsilon, 1) / simpson_with_limit(k, epsilon, 2)
    return c


def chebyshev_approximation(n, a, b, epsilon):
    # Chebyshev coefficients
    c = chebyshev_coefficients2(n, epsilon)
    # c = chebyshev_coefficients(n)

    x = np.linspace(a, b, 1001)
    p = np.zeros(x.size)
    # Chebyshev polynomial approximation of f
    for i in range(x.size):
        for k in range(c.size):
            p[i] += c[k] * chebyshev_polynomial(x[i], k)
    err = np.sqrt(simpson_error(p, x, a, b))
    return p, x, err
