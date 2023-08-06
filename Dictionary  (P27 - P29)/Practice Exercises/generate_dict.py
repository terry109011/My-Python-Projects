def generate_dictionary(num):
    dictionary = {}
    while True:
        try:
            num = int(num)
            if num > 0:
                for i in range(1, num + 1):
                    dictionary[i] = i**2
                return dictionary
            else:
                print('Input must be a positive integer.')
                return None
        except ValueError:
            print('Input must be a positive integer.')
            return None
        
my_dict = generate_dictionary(6)
print(my_dict)