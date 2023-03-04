import math
from matplotlib import pyplot as plt
import functions as f


class Main:
    defined_functions = {
        '1': f.polynomial,
        '2': f.trigonometric,
        '3': f.exponent_func,
        '11': f.polynomial_derivative,
        '22': f.trigonometric_derivative,
        '33': f.exponent_derivative,
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
        fp1 = defined_functions[2 * user_functions[0]]
        fp2 = defined_functions[2 * user_functions[1]]

        print(f'Metoda bisekcji: {f.bisection(f1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2)}')
        print(
            f'Metoda stycznych: {f.newton_method(f1, fp1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, fp2=fp2)}')
