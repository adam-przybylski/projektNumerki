import math
from matplotlib import pyplot as plt

class main:
    if __name__ == "__main__":
        func_count = input("Podaj ilość funkcji w twoim złożeniu: ")
        lower_bound = input("Podaj dolny przedział poszukiwania miejsca zerowego: ")
        upper_bound = input("Podaj górny przedział poszukiwania miejsca zerowego: ")
        stop_criterion = input("Podaj warunek stopu: 1 - epsilon, 2 - ilośc iteracji: ")
        if stop_criterion == "1":
            epsilon = input("Podaj wartość epsilonu: ")
        elif stop_criterion == "2":
            iteration_number = input("Podaj ilość iteracji: ")
        else:
            exit(1)

        user_functions = []

        for i in  range(int(func_count)):
            print('''Wybierz funkcje z których chcesz otrzymać złożenie:
            1 - Wielomian
            2 - Funkcje trygonometryczną
            3 - Funkcje wykładniczą''')
            user_fn = input()
            user_functions.append(user_fn)

        print(user_functions)
# defined_functions = {
#     "poli": 1,
#     "trygon"
# }

def polynomial(x):
    x3 = x * x * x
    return x3 - x + 1


def bisection(epsilon, interval_beg, interval_end):
    solutions = []



