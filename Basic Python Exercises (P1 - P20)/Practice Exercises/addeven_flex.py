# Implement a function which takes two parameters as start and end of range and returns sum of even numbers within given range.

def add_even_numbers(start, end):
    even_sum = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            even_sum += number
    return even_sum

print(add_even_numbers(4, 10))

