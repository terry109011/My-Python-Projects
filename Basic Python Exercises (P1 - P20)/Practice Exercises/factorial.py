
def my_factorial(n):
    if n == 0:
        print('Invalid input')
        factorial = None
    else:
        factorial = 1
        for i in range(1,n+1):
            factorial *= i
    return factorial

print(my_factorial(0))
    