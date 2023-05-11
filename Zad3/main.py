import functions as f
import numpy as np
from matplotlib import pyplot as plt


def main():
    defined_functions = {
        '1': np.sin,
        '2': np.tan,
    }

    user_functions = [None, None, None]

    func_count = int(input("Podaj liczbę funkcji w twoim złożeniu (max 3): "))
    if func_count > 3:
        print("Przekroczono limit funkcji do złożenia.")
        exit(1)
    for i in range(func_count):
        print('''Wybierz funkcje z których chcesz otrzymać złożenie:
                1 - Wielomian
                2 - Funkcje trygonometryczną
                3 - Funkcje liniową
                4 - |x|''')
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
                                2 - tg(x)''')
            user_choice = input()
            if user_choice not in defined_functions.keys():
                print("Nie ma takiego wyboru.")
                exit(-1)
            user_functions[i] = defined_functions[user_choice]
        elif func_type == '3':
            f.a = float(input("Wybierz współczynnik 'a' funkcji liniowej: "))
            f.b = float(input("Wybierz współczynnik 'b' funkcji liniowej: "))
            user_functions[i] = f.linear
        elif func_type == '4':
            user_functions[i] = f.x_abs
        else:
            print("Wybrano złą funkcję.")
            exit(-1)
    a = float(input("Podaj początek przedziału interpolacji: "))
    b = float(input("Podaj koniec przedziału interpolacji: "))
    n = int(input("Podaj liczbę węzłów interpolacyjnych: "))

    f3 = user_functions[2]
    f2 = user_functions[1]
    f1 = user_functions[0]

    interp_nodes_x = np.linspace(a, b, num=n)
    interp_nodes_y = f.nested_function(f1, interp_nodes_x, f2, f3)

    # computing actual values of a function
    x_true = np.linspace(a, b, num=1000)
    y_true = f.nested_function(f1, x_true, f2, f3)

    # INTERPOLATION
    xi = np.linspace(a, b, num=100)
    yi = np.zeros(xi.size)

    for i in range(xi.size):
        yi[i] = f.lagrange_interp(interp_nodes_x, interp_nodes_y, xi[i])


    # plot section
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
    ax.scatter(interp_nodes_x, interp_nodes_y, color='red', label="węzły")
    # xlist = np.linspace(0, 5, num=1000)
    ax.plot(xi, yi, color='green', label="wielomian interpolacyjny")
    ax.plot(x_true, y_true, color='blue', label="pierwotna funkcja")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()


