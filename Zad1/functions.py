import decimal
import math


def bisection(f1, a, b, f2=None, epsilon=None, iteration_number=None):
    if f2 is not None:
        if epsilon is not None:
            x1 = (a + b) / 2
            x1, a, b = bisection_algorithm(a, b, x1, f1(f2(a)), f1(f2(x1)))
            x2 = (a + b) / 2
            x2, a, b = bisection_algorithm(a, b, x2, f1(f2(a)), f1(f2(x2)))
            i = 2
            while abs(x2 - x1) >= epsilon:
                x1 = x2
                x2 = (a + b) / 2
                x2, a, b = bisection_algorithm(a, b, x2, f1(f2(a)), f1(f2(x2)))
                i += 1
            return x2, i
        else:
            x1 = None
            for i in range(iteration_number):
                x1 = (a + b) / 2
                x1, a, b = bisection_algorithm(a, b, x1, f1(f2(a)), f1(f2(x1)))
            return x1
    else:
        if epsilon is not None:
            x1 = (a + b) / 2
            x1, a, b = bisection_algorithm(a, b, x1, f1(a), f1(x1))
            x2 = (a + b) / 2
            x2, a, b = bisection_algorithm(a, b, x2, f1(a), f1(x2))
            i = 2
            while abs(x2 - x1) >= epsilon:
                x1 = x2
                x2 = (a + b) / 2
                x2, a, b = bisection_algorithm(a, b, x2, f1(a), f1(x2))
                i += 1
            return x2, i
        else:
            x1 = None
            for i in range(iteration_number):
                x1 = (a + b) / 2
                x1, a, b = bisection_algorithm(a, b, x1, f1(a), f1(x1))
            return x1


def bisection_algorithm(a, b, x1, func1, func2):
    if func1 * func2 < 0:
        b = x1
    else:
        a = x1
    return x1, a, b
