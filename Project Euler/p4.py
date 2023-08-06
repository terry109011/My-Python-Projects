def ispalindrome(num : int):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
            prod = i*j
            if (prod > largest and ispalindrome(prod) == True):
                largest = prod

print(largest)
