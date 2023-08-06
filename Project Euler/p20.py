def factorial(n):
    if n <= 0:
        return 'Positive value only'
    prod = n
    while n > 1:
        prod *= n - 1
        n -= 1
    return prod
    
result = str(factorial(100))
sum = 0
for n in result:
    sum += int(n)
print(sum)