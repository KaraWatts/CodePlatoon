def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(1))       # 1
print(factorial(5))       # 120
print(factorial(100))     # 9.332621544394418e+157
