import functions as f
import numpy as np
import time


def main():
    defined_functions = {
        '1': np.sin,
        '2': np.tan,
    }
    global epsilon
    user_functions = [None, None, None]
    print("Witaj w programie do całkowania numerycznego!")
    epsilon = float(input("Podaj dokładność dla metody Simpsona: "))
    func_count = int(input("Podaj liczbę funkcji w twoim złożeniu (max 3): "))
    if func_count > 3:
        print("Przekroczono limit funkcji do złożenia.")
        exit(1)
    for i in range(func_count):
        print('''Wybierz funkcje z których chcesz otrzymać złożenie:
                    1 - Wielomian
                    2 - Funkcje trygonometryczną
                    3 - Funkcje liniową
                    4 - Funkcja wykładnicza''')
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
            f.a_linear = float(input("Wybierz współczynnik 'a' funkcji liniowej: "))
            f.b_linear = float(input("Wybierz współczynnik 'b' funkcji liniowej: "))
            user_functions[i] = f.linear
        elif func_type == '4':
            f.exponent_base = float(input("Wybierz podstawę funkcji wykładniczej: "))
            user_functions[i] = f.exponent
        else:
            print("Wybrano złą funkcję.")
            exit(-1)

    f3 = user_functions[2]
    f2 = user_functions[1]
    f1 = user_functions[0]

    S = f.simpson_with_limit(f1, f2, f3, epsilon)
    print(f'Metoda Simpsona: {S}')
    print("Metoda Gaussa-Czebyszewa:")
    print(f'    2 węzły: {f.gauss_chebyshev(f1, f2, f3, 2)}')
    print(f'    3 węzły: {f.gauss_chebyshev(f1, f2, f3, 3)}')
    print(f'    4 węzły: {f.gauss_chebyshev(f1, f2, f3, 4)}')
    print(f'   5 węzłów: {f.gauss_chebyshev(f1, f2, f3, 5)}')
    return


if __name__ == '__main__':
    main()
