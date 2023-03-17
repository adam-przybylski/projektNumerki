import math
import numpy as np

poly_args = []
exponent_base = 0


def horner(x, args):
    result = 0
    for coefficient in args:
        result = result * x + coefficient
    return result


def polynomial(x):
    return horner(x, poly_args)


def polynomial_derivative(x):
    deriv_args = []
    degree = len(poly_args) - 1
    for i in range(degree):
        deriv_args.append(poly_args[i] * (degree - i))
    return horner(x, deriv_args)


def avg(x1, x2):
    return (x1 + x2) / 2


def ctan(x):
    return 1 / np.tan(x)


def exponent_func(x):
    return exponent_base ** x - 1


def exponent_derivative(x):
    return math.log(exponent_base, math.e) * exponent_base ** x


def nested_function(f1, x, f2=None, f3=None):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))


def cos_deriv(x):
    return -np.sin(x)


def tan_deriv(x):
    return 1.0 / (np.cos(x) ** 2)


def ctan_deriv(x):
    return -1.0 / (np.sin(x) ** 2)


def bisection_algorithm(a, b, x1, func1, func2):
    if func1 * func2 < 0:
        b = x1
    else:
        a = x1
    return a, b


def bisection(f1, a, b, f2=None, f3=None, epsilon=None, iteration_number=None):
    if (nested_function(f1, a, f2, f3) <= 0 and nested_function(f1, b, f2, f3) <= 0) or (
            nested_function(f1, a, f2, f3) >= 0 and nested_function(f1, b, f2, f3) >= 0):
        raise Exception
    if epsilon is not None:
        x1 = avg(a, b)
        if nested_function(f1, x1, f2, f3) == 0:
            return x1, 1
        a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        x2 = avg(a, b)
        if abs(x2 - x1) < epsilon:
            return x1, 2
        a, b = bisection_algorithm(a, b, x2, nested_function(f1, a, f2, f3), nested_function(f1, x2, f2, f3))
        i = 2
        while abs(x2 - x1) >= epsilon:
            x1 = x2
            x2 = avg(a, b)
            a, b = bisection_algorithm(a, b, x2, nested_function(f1, a, f2, f3), nested_function(f1, x2, f2, f3))
            i += 1
        return x2, i
    else:
        x1 = avg(a, b)
        if nested_function(f1, x1, f2, f3) == 0:
            return x1, 1
        a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        for i in range(1, iteration_number):
            x1 = avg(a, b)
            a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        return x1, iteration_number


def derivative(f):
    if f == polynomial:
        return polynomial_derivative
    if f == np.sin:
        return np.cos
    if f == np.cos:
        return cos_deriv
    if f == np.tan:
        return tan_deriv
    if f == ctan:
        return ctan_deriv
    if f == exponent_func:
        return exponent_derivative


def nested_function_derivative(fp1, x, fp2=None, fp3=None, f2=None, f3=None):
    if fp2 is None:
        return fp1(x)
    if fp3 is None:
        return fp1(f2(x)) * fp2(x)
    else:
        return fp1(f2(f3(x))) * fp2(f3(x)) * fp3(x)


def newton_method(f1, fp1, a, b, f2=None, fp2=None, f3=None, fp3=None, epsilon=None, iteration_number=None):
    x1 = avg(a, b)
    deriv = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
    if deriv == 0:
        raise Exception
    x2 = x1 - nested_function(f1, x1, f2, f3) / deriv
    if epsilon is not None:
        i = 1
        while abs(x2 - x1) >= epsilon:
            x1 = x2
            deriv = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
            if deriv == 0:
                raise Exception
            x2 = x1 - nested_function(f1, x1, f2, f3) / deriv
            i += 1
        return x2, i
    else:
        for i in range(1, iteration_number):
            x1 = x2
            deriv = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
            if deriv == 0:
                raise Exception
            x2 = x1 - nested_function(f1, x1, f2, f3) / deriv
        return x2, iteration_number
