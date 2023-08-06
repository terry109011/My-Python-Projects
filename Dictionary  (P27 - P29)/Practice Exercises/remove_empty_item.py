# Remove empty items

# Implement a function which takes as a parameter dictionary and removes
# empty items from it and return new dictionary. If there is not any empty
# item in the dictionary it will return itself.

# Example:
    
# custom_dict = {
#     "name" : "Elshad",
#     "age" : 28,
#     "city" : None
# }
# remove_empty_items(custom_dict)

# Output:
# {'name': 'Elshad', 'age': 28}

def remove_empty_items(custom_dict):
    
    '''Must convert custom_dict.items() to a list
       because custom_dict.items() alone is just a
       view object, which cannot be modified. '''
       
    for key, value in list(custom_dict.items()):
        if value == " " or value == None:
            del custom_dict[key]
    return custom_dict

custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None
}

print(remove_empty_items(custom_dict))

