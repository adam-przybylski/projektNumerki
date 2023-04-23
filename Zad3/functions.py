import numpy as np

poly_args = []
a = 0
b = 0


def horner(x, args):
    result = 0
    for coefficient in args:
        result = result * x + coefficient
    return result


def polynomial(x):
    return horner(x, poly_args)


def linear(x):
    return a * x + b


def x_abs(x):
    return abs(x)


def nested_function(f1, x, f2=None, f3=None):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))


# def read_from_file(name):
#     with open(name, "r") as file:
#         lines = file.readlines()
#         x_array = lines[0].strip().split(" ")
#     return x_array


def lagrange_interp(x, y, xi):
    n = len(x)
    li = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                li[i] *= (xi - x[j])/(x[i] - x[j])
    yi = np.sum(y * li)
    return yi
