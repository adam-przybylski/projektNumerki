import math
from matplotlib import pyplot as plt


def polynomial(x):
    x3 = x * x * x
    return x3 - x + 1


def bisection(epsilon, interval_beg, interval_end):
    solutions = []



