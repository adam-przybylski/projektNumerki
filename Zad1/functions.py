import math


# zrobić średnią
# schemat Hornera

def polynomial(x):
    x2 = x ** 2
    return x2 - x - 1


def trigonometric(x):
    return math.cos(x)


def exponent_func(x):
    a = 2
    return a ** x


def polynomial_derivative(x):
    return 2 * x - 1


def trigonometric_derivative(x):
    return -math.sin(x)


def exponent_derivative(x):
    return math.log(2, math.e) * 2 ** x


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


def newton_method(f1, fp1, a, b, f2=None, fp2=None, epsilon=None, iteration_number=None):
    x1 = (a + b) / 2
    x2 = x1 - f1(x1) / fp1(x1)
    if f2 is not None:
        if epsilon is not None:
            i = 2
            while abs(x2 - x1) >= epsilon:
                x1 = x2
                x2 = x1 - f1(f2(x1)) / (fp1(f2(x1)) * fp2(x1))
                i += 1
            return x2, i
        else:
            for i in range(2, iteration_number):
                x1 = x2
                x2 = x1 - f1(f2(x1)) / (fp1(f2(x1)) * fp2(x1))
            return x2
    else:
        if epsilon is not None:
            i = 2
            while abs(x2 - x1) >= epsilon:
                x1 = x2
                x2 = x1 - f1(x1) / fp1(x1)
                i += 1
            return x2, i
        else:
            for i in range(2, iteration_number):
                x1 = x2
                x2 = x1 - f1(x1) / fp1(x1)
            return x2
