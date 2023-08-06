# Multiply Dictionary Items

# Implement a function which takes dictionary as a parameter
# and returns multiplication of values of this dictionary.

my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}

def multiply_values(my_dict):
    output = 1
    for keys in my_dict:
        output *= my_dict[keys]
    return output

print(multiply_values(my_dict))