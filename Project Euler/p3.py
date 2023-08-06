from math import sqrt

def check_prime(val):
    for i in range(2, int(val/2)):
        if val % i == 0:
            return False
    return True
'''
The reason why for loop upper limit is val / 2 is
val is not divisible by any number > n / 2, the division
will always be 1 accompanied by a remainer.
'''
# rewrite, without library

def max_primeft(val):
    max_primeft = 0
    if val % 2 == 0:
        return 'Not prime'
    for i in range(3, int(sqrt(val)) , 2):
        if val % i == 0:
            if check_prime(i) == True:
                if i > max_primeft:
                    max_primeft = i
    return max_primeft

# print(max_primeft(15))

'''
All prime numbers are odd, except 2. Hence,
the for loop starts from 3 and increment by
2. The upper limit is sqrt(val) is because

val = sqrt(val) * sqrt(val) where two factors
equal each other.

Assume F1 and F2 are prime:

Apart from the above, factor pair of a number 'val'
contains two numbers F1 < sqrt(val) and F2 > sqrt(val).
If 'val' is divisible by F1, then we know 'val' is 
also divisible by F2. Therefore, we don't need to 
check for divisibility of any number greater than
sqrt(val) since a divisor will definitely appear.
In this case, 'val' is proved to be not prime.

The greatest prime factor is the largest F1.

Example: mirror factor pairs of 40

val = 40

1 40 - pair 1
2 20 - pair 2
4 10 - pair 3
5 8  - pair 4

sqrt(40) = 6.32

8 5  - p4
10 4 - p3
20 2 - p2
40 1 - p1

'''

# BEST SOLUTION
# n = 600851475143
# n = 170
# i = 2

# while i * i < n:
#     while n % i == 0:
#         n = n / i
#     i = i + 1
    
# print(n)

