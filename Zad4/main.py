import functions as f
import numpy as np
import time


def main():
    start = time.time()
    f.a_linear = 2
    f.b_linear = 1
    f.poly_args = [1, -1, 1]
    S = f.simpson(f.polynomial, 0, 4, 0.001)
    print(S)
    end = time.time()
    print(f'Elapsed time: {end - start} seconds')


if __name__ == '__main__':
    main()
