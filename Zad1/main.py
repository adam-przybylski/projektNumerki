import numpy as np
from matplotlib import pyplot as plt
import functions as f


class Main:
    defined_functions = {
        '1': np.sin,
        '2': np.cos,
        '3': np.tan,
        '4': f.ctan
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
            func_type = input()
            if func_type == '1':
                degree = int(input("Podaj stopień wieolomianu: "))
                print("Podaj współczynniki wielomianu (od najwyższego do najniższego)")
                for j in range(degree + 1):
                    a = float(input(f'Podaj {j + 1} współczynnik: '))
                    f.poly_args.append(a)
                user_functions[i] = f.polynomial
            elif func_type == '2':
                print('''Wybierz funkcje trygonometryczną:
                            1 - sin(x)
                            2 - cos(x)
                            3 - tg(x)
                            4 - ctg(x)''')
                user_choice = input()
                if user_choice not in defined_functions.keys():
                    print("Nie ma takiego wyboru.")
                    exit(-1)
                user_functions[i] = defined_functions[user_choice]
            elif func_type == '3':
                f.exponent_base = float(input("Wybierz podstawę funkcji wykładniczej: "))
                user_functions[i] = f.exponent_func
            else:
                print("Wybrano złą funkcję.")
                exit(-1)

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

        f3 = user_functions[2]
        f2 = user_functions[1]
        f1 = user_functions[0]
        if f1 is not None:
            fp1 = f.derivative(f1)
        if f2 is not None:
            fp2 = f.derivative(f2)
        if f3 is not None:
            fp3 = f.derivative(f3)

        # Plot section
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        ticks_frequency = 1

        fig, ax = plt.subplots(figsize=(10, 10))

        fig.patch.set_facecolor('#ffffff')

        ax.set(xlim=(a - 2, b + 2), ylim=(ymin - 1, ymax + 1), aspect='equal')

        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
        ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)

        x_ticks = np.arange(a, b + 1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
        ax.set_xticks(x_ticks[x_ticks != 0])
        ax.set_yticks(y_ticks[y_ticks != 0])
        ax.set_xticks(np.arange(a, b + 1), minor=True)
        ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        xlist = np.linspace(a, b, num=1000)
        ax.plot(xlist, f.nested_function(f1, xlist, f2, f3), color='blue')

        try:
            result = f.bisection(f1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, f3=f3)
            ax.plot(result[0], 0, "ro",  label="Bisection method")
            print(
                f'Metoda bisekcji: {result}')
        except Exception:
            print("Aby wykonać poszukiwanie miejsca zerowego metodą bisekcji funkcja na krańcach przedziału musi mieć "
                  "różne znaki")
            pass

        try:
            result = f.newton_method(f1, fp1, a, b, epsilon=epsilon, iteration_number=iteration_number, f2=f2, fp2=fp2,
                                     f3=f3, fp3=fp3)
            ax.plot(result[0], 0, "go", label="Newton method")
            print(
                f'Metoda stycznych: {result}')
        except Exception:
            print("Nie można dokończyć algorytmu bo jedna z pochodnych jest równa 0")
            pass
        ax.legend()
        plt.show()
