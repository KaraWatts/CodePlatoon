def factorial(n):
    result = 1

    for i in range(n, 1, -1):
        result *= i

    return result


print(factorial(1))       # 1
print(factorial(5))       # 120
print(factorial(100))     # 9.332621544394418e+157
