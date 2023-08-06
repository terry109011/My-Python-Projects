msum = 0

def factorise(num):
    c = 0
    for j in range(1, int(num/2) + 1):
        if num % j == 0:
            c += 1
    return c

n = 15000000000
print(factorise(n))
