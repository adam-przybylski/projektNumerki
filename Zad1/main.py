import math
from matplotlib import pyplot as plt
import functions as f


def polynomial(x):
    x2 = x ** 2
    return x2 - x - 1


def trigonometric(x):
    return math.cos(x)


def exponent_func(x):
    a = 2
    return a ** x


class Main:
    defined_functions = {
        '1': polynomial,
        '2': trigonometric,
        '3': exponent_func,
        None: None
    }

    epsilon = None
    iteration_number = None
    user_functions = [None, None]

    if __name__ == "__main__":

        func_count = input("Podaj ilość funkcji w twoim złożeniu: ")
        for i in range(int(func_count)):
            print('''Wybierz funkcje z których chcesz otrzymać złożenie:
            1 - Wielomian
            2 - Funkcje trygonometryczną
            3 - Funkcje wykładniczą''')
            user_fn = input()
            user_functions[i] = user_fn
        print(user_functions)
        a = float(input("Podaj dolny przedział poszukiwania miejsca zerowego: "))
        b = float(input("Podaj górny przedział poszukiwania miejsca zerowego: "))

        stop_criterion = input("Podaj warunek stopu: 1 - epsilon, 2 - ilośc iteracji: ")
        if stop_criterion == "1":
            epsilon = float(input("Podaj wartość epsilonu: "))
        elif stop_criterion == "2":
            iteration_number = int(input("Podaj ilość iteracji: "))
        else:
            print("Złe kryterium")
            exit(1)

        f2 = defined_functions[user_functions[1]]
        f1 = defined_functions[user_functions[0]]

        print(f.bisection(f1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2))
