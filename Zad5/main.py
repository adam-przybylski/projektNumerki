import functions as f
import numpy as np
from matplotlib import pyplot as plt


def main():
    global degree, a, b, epsilon
    defined_functions = {
        '1': np.sin,
        '2': np.tan,
    }
    user_functions = [None, None, None]
    print("Witaj w programie do całkowania numerycznego!")
    func_count = int(input("Podaj liczbę funkcji w twoim złożeniu (max 3): "))
    if func_count > 3:
        print("Przekroczono limit funkcji do złożenia.")
        exit(1)
    for i in range(func_count):
        print('''Wybierz funkcje z których chcesz otrzymać złożenie:
                    1 - Wielomian
                    2 - Funkcja trygonometryczną
                    3 - Funkcja |x|
                    4 - Funkcja wykładnicza''')
        func_type = input()
        if func_type == '1':
            degree = int(input("Podaj stopień wieolomianu: "))
            print("Podaj współczynniki wielomianu (od najwyższego do najniższego)")
            for j in range(degree + 1):
                temp = float(input(f'Podaj {j + 1} współczynnik: '))
                f.poly_args.append(temp)
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
            user_functions[i] = np.abs
        elif func_type == '4':
            f.exponent_base = float(input("Wybierz podstawę funkcji wykładniczej: "))
            user_functions[i] = f.exponent
        else:
            print("Wybrano złą funkcję.")
            exit(-1)
    a = float(input("Podaj początek przedziału aproksymacji: "))
    b = float(input("Podaj koniec przedziału aproksymacji: "))
    degree = int(input("Podaj stopień wielomianu aproksymacyjnego: "))
    epsilon = float(input("Podaj dokładność dla metody Simpsona: "))

    f.f3 = user_functions[2]
    f.f2 = user_functions[1]
    f.f1 = user_functions[0]

    p, x, err = f.chebyshev_approximation(degree, a, b, epsilon)
    y = f.nested_function(x)

    print(f'Błąd aproksymacji: {err}')
    # plot section
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
    ax.set_xlabel('$x$', size=14, labelpad=-24, x=1.02)
    ax.set_ylabel('$y$', size=14, labelpad=-21, y=1.02, rotation=0)
    ax.plot(x, y, color='blue', label="pierwotna funkcja")
    ax.plot(x, p, color='green', label="funkcja aproksymowana")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
