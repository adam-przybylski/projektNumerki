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
            1 - Wielomian f(x) = x^2 - x - 1
            2 - Funkcje trygonometryczną f(x) = cos(x)
            3 - Funkcje wykładniczą f(x) = 2^x''')
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

        try:
            print(
                f'Metoda bisekcji: {f.bisection(f1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, f3=f3)}')
        except Exception:
            print("Aby wykonać poszukiwanie miejsca zerowego metodą bisekcji funkcja na krańcach przedziału musi mieć "
            "różne znaki")
            pass

        try:
            print(
                f'Metoda stycznych: {f.newton_method(f1, fp1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, fp2=fp2, f3=f3, fp3=fp3)}')
        except Exception:
            print("Nie można dokończyć algorytmu bo jedna z pochodnych jest równa 0")
            pass

        # Plot section
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        ticks_frequency = 1

        fig, ax = plt.subplots(figsize=(10, 10))

        fig.patch.set_facecolor('#ffffff')

        ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
        ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

        x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])
        ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        xlist = np.linspace(-5, 5, num=1000)
        plt.plot(xlist, f.nested_function(f1, xlist, f2, f3), color='red')
        plt.show()
