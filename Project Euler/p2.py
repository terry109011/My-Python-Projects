def evenfib_sum(val):
    a = 1
    b = 2
    fib_sum = a + b
    even_sum = 2
    while fib_sum <= val:
        a = b
        b = fib_sum
        fib_sum = a + b
        if fib_sum % 2 == 0:
            even_sum += fib_sum    
    return even_sum

print(evenfib_sum(10))
        