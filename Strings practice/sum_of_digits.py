def sum_of_digits(num):
    num_len = len(num)
    my_sum = 0
    for i in range(1, num_len + 1):
        my_sum += int(num[i-1])
    return my_sum


while True:
    try:
        num = input('Enter a number: ')
        new_sum = sum_of_digits(num)
        print(new_sum)
        break
    except ValueError:
        print('Numerical Inputs only, please try again')
        continue