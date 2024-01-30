from random import randint
import time
import matplotlib.pyplot as plt


def constant(N):
    results = {}
    for n in N:

        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(1) - constant
        # ------------------------------------------

        value = array[0]
        print(value)

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle


def logarithmic(N):
    results = {}
    for n in N:

        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(log(n)) - logarithmic
        # ------------------------------------------

        index = binary_search(array, 1)
        print(index)

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def linear(N):
    results = {}
    for n in N:

        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(n) - linear
        # ------------------------------------------

        sum = 0
        for number in array:
            sum += number

        print(sum)

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def quadratic(N):
    results = {}
    for n in N:
        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(n^2) - quadratic
        # ------------------------------------------

        r = []
        for number in array:
            for num in array:
                r.append(number + num)

        print(len(r))

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def logLinear(N):
    results = {}
    for n in N:
        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(n log n) - quasilinear
        # ------------------------------------------
        r = []

        for value in array:
            r.append(binary_search(array, value))

        print(len(r))

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


def exponential(N):
    results = {}
    for n in N:
        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(2^n) - Exponential
        # ------------------------------------------

        print(Fibonacci(n))

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def f(n):
    if (n == 0):
        print('*******')
        return

    for i in range(n):
        f(n-1)


def factorial(N):
    results = {}
    for n in N:
        array = list(range(n))
        start = time.time()
        time.sleep(1)

        #
        # O(n log n) - Exponential
        # ------------------------------------------

        f(n)

        # -------------------------------------------
        #

        end = time.time()
        results[n] = end - start

    return results


def print_results(complexity, results):
    print('complexity: ', complexity)

    print(f'n        time elapsed')
    for r in results:
        print(f'{r}       {results[r]} ')


N = [10, 20, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
N2 = [10, 20, 100, 1000, 10000, 100000, 1000000, 5000000]
N3 = [10, 20, 100, 1000, 10000]
N4 = [10, 20, 40]
N5 = [3, 6, 9]

print_results('O(1)', constant(N))
# print_results('O(log n)', logarithmic(N))
# print_results('O(n)', linear(N))
# print_results('O(n log n)', logLinear(N2))
# print_results('O(n^2)', quadratic(N3))
# print_results('O(2^n)', exponential(N4))
# print_results('O(n!)', factorial(N5))
