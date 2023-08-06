# Implement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.

def add_odd_numbers():
    odd_sum = 0
    for i in range(1,101,2):
        odd_sum += i
    return odd_sum

print(add_odd_numbers())