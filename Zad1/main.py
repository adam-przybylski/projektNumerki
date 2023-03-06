import numpy as np
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
    user_functions = [None, None, None]
    fp1 = None
    fp2 = None
    fp3 = None

    if __name__ == "__main__":
        func_count = int(input("Podaj liczbę funkcji w twoim złożeniu (max 3): "))
        if func_count > 3:
            print("Przekroczono limit funkcji do złożenia.")
            exit(1)
        for i in range(func_count):
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
            print("Zły warunek stopu")
            exit(1)

        f3 = defined_functions[user_functions[2]]
        f2 = defined_functions[user_functions[1]]
        f1 = defined_functions[user_functions[0]]
        if user_functions[0] is not None:
            fp1 = defined_functions[2 * user_functions[0]]
        if user_functions[1] is not None:
            fp2 = defined_functions[2 * user_functions[1]]
        if user_functions[2] is not None:
            fp3 = defined_functions[2 * user_functions[2]]

        if (f.nested_function(f1, a, f2, f3) < 0 and f.nested_function(f1, b, f2, f3) < 0) or (
                f.nested_function(f1, a, f2, f3) > 0 and f.nested_function(f1, b, f2, f3) > 0):
            print(
                "Aby wykonać poszukiwanie miejsca zerowego metodą bisekcji funkcja na krańcach przedziału musi mieć "
                "różne znaki")
        else:
            print(
                f'Metoda bisekcji: {f.bisection(f1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, f3=f3)}')

        print(
            f'Metoda stycznych: {f.newton_method(f1, fp1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, fp2=fp2, f3=f3, fp3=fp3)}')

        # plt.rcParams["figure.figsize"] = [7.50, 7.50]
        # plt.rcParams["figure.autolayout"] = True

        xlist = np.linspace(-5, 5, num=1000)
        # xlist = np.arange(-10, 10.1, .1, )

        plt.figure(num=0, dpi=120)
        plt.plot(xlist, f.nested_function(f1, xlist, f2, f3), color='red')
        plt.show()
