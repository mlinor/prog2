#!/usr/bin/env python3

from person import Person
from numba import njit
from time import perf_counter as pc
import matplotlib.pyplot as plt

def fib_py(n):
    if n <= 1:
        return n
    else:
        return fib_py(n-1) + fib_py(n-2)

@njit
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return fib_numba(n-1) + fib_numba(n-2)

def main():
    f = Person(5)
    print(f.get())
    f.set(7)
    print(f.get())


    py = []
    cpp = []
    nba = []
    for x in range(20, 31):
        start = pc()
        fib_py(x)
        end = pc()
        py.append(end - start)
    
    for x in range(20,31):
        start = pc()
        fib_numba(x)
        end = pc()
        nba.append(end - start)

    f = Person(0)
    for x in range(30,46):
        start = pc()
        f.set(x)
        f.fib()
        end = pc()
        cpp.append(end - start)

    plt.scatter(list(range(20,31)), py, color='red', label='Python')
    plt.scatter(list(range(30,46)), cpp, color='yellow', label='Cpp')
    plt.scatter(list(range(20,31)), nba, color='blue', label='Numba')
    
    plt.legend()

    plt.xlabel('n')
    plt.ylabel('Time (seconds)')

    plt.savefig('Results.png')

    plt.show()
    
    start = pc()
    f.set(47)
    f.fib()
    end = pc()
    print(f"Cost time of CPP code when n = 47: {end - start}")
    
    start = pc()
    fib_numba(47)
    end = pc()
    print(f"Cost time of numba code when n = 47: {end - start}")

if __name__ == '__main__':
	main()
