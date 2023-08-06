# Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5 and if a number is 
# greater than 130 display STOP in the console.

list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 

def numbers_divisible_byfive(a_list):
    for element in a_list:
        if element % 5 == 0:
            print(element)
        if element >= 130:
            break
    print('STOP')
    
numbers_divisible_byfive(list1)
