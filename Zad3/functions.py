poly_args = []


def horner(x, args):
    result = 0
    for coefficient in args:
        result = result * x + coefficient
    return result


def polynomial(x):
    return horner(x, poly_args)


def nested_function(f1, x, f2=None, f3=None):
    if f2 is None:
        return f1(x)
    if f3 is None:
        return f1(f2(x))
    else:
        return f1(f2(f3(x)))
