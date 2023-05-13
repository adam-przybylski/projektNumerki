import functions as f
import numpy as np
import time


def main():
    global epsilon
    func = None
    print("Witaj w programie do całkowania numerycznego!")
    epsilon = float(input("Podaj dokładność dla metody Simpsona: "))
    print("""Jaka funkcja wariacie?
                1: Liniowa
                2: Wielomianowa
                3: Sinus
                4: Cosinus""")
    fn_number = input()
    match fn_number:
        case "1":
            f.a_linear = float(input("Podaj parametr a: "))
            f.b_linear = float(input("Podaj parametr b: "))
            func = f.linear
        case "2":
            n = int(input("Podaj stopien wielomianu: "))
            for i in range(n + 1):
                f.poly_args.append(float(input(f'Podaj wspolczynnik nr {i + 1}: ')))
            func = f.polynomial
        case "3":
            func = np.sin
            return
        case "4":
            func = np.cos
            return

    S = f.simpson_with_limit(func, epsilon)
    print(f'Metoda Simpsona: {S}')
    print("Metoda Gaussa-Czebyszewa:")
    print(f'    2 węzły: {f.gauss_chebyshev(func, 2)}')
    print(f'    3 węzły: {f.gauss_chebyshev(func, 3)}')
    print(f'    4 węzły: {f.gauss_chebyshev(func, 4)}')
    print(f'   5 węzłów: {f.gauss_chebyshev(func, 5)}')
    return


if __name__ == '__main__':
    main()
