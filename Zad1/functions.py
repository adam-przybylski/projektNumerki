import math
import numpy as np

poly_args = []
exponent_base = 0


def horner(x):
    result = 0
    for coefficient in poly_args:
        result = result * x + coefficient
    return result


def avg(x1, x2):
    return (x1 + x2) / 2


def ctan(x):
    return 1 / np.tan(x)


def exponent_func(x):
    return exponent_base ** x


def polynomial_derivative(x):
    return horner(x)


def trigonometric_derivative(x):
    return -np.sin(x)


def exponent_derivative(x):
    return math.log(2, math.e) * 2 ** x


def nested_function(f1, x, f2=None, f3=None):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))


def bisection_algorithm(a, b, x1, func1, func2):
    if func1 * func2 < 0:
        b = x1
    else:
        a = x1
    return a, b


def bisection(f1, a, b, f2=None, f3=None, epsilon=None, iteration_number=None):
    if (nested_function(f1, a, f2, f3) < 0 and nested_function(f1, b, f2, f3) < 0) or (
            nested_function(f1, a, f2, f3) > 0 and nested_function(f1, b, f2, f3) > 0):
        raise Exception
    if epsilon is not None:
        x1 = avg(a, b)
        a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        x2 = avg(a, b)
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
        a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        for i in range(1, iteration_number):
            x1 = avg(a, b)
            a, b = bisection_algorithm(a, b, x1, nested_function(f1, a, f2, f3), nested_function(f1, x1, f2, f3))
        return x1, iteration_number


def nested_function_derivative(fp1, x, fp2=None, fp3=None, f2=None, f3=None):
    if fp2 is None:
        return fp1(x)
    if fp3 is None:
        return fp1(f2(x)) * fp2(x)
    else:
        return fp1(f2(f3(x))) * fp2(f3(x)) * fp3(x)


def newton_method(f1, fp1, a, b, f2=None, fp2=None, f3=None, fp3=None, epsilon=None, iteration_number=None):
    x1 = avg(a, b)
    derivative = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
    if derivative == 0:
        raise Exception
    x2 = x1 - nested_function(f1, x1, f2, f3) / derivative
    if epsilon is not None:
        i = 2
        while abs(x2 - x1) >= epsilon:
            x1 = x2
            derivative = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
            if derivative == 0:
                raise Exception
            x2 = x1 - nested_function(f1, x1, f2, f3) / derivative
            i += 1
        return x2, i
    else:
        for i in range(2, iteration_number):
            x1 = x2
            derivative = nested_function_derivative(fp1, x1, fp2, fp3, f2, f3)
            if derivative == 0:
                raise Exception
            x2 = x1 - nested_function(f1, x1, f2, f3) / derivative
        return x2, iteration_number
