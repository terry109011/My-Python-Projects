from math import sqrt

a = 0
b = 0

for i in range(1,1000):
    for j in range(1, 1000):
        if (1000*(i + j) - i*j == 500000 and i < j):
            a = i
            b = j
            
def check_pysum(a, b):
    c_square = a*a + b*b
    c = int(sqrt(c_square))
    if (a + b + c == 1000):
        return f'a = {a} \nb = {b} \nc = {c}\na*b*c = {a*b*c}'
    return 'Not pythagorean sum'

print(check_pysum(a,b))