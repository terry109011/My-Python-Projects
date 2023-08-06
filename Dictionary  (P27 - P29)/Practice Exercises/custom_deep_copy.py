# Custom Deep Copy for List Values

# Implement custom deep copy method for a dictionary where the values are lists.

# Example:
# original_dict = {
#     "names" : ["Elshad", "John", "Edy"],
#     "numbers" : [1,2,3,4,5]
# }
 
# copied_dict = deep_copy(original_dict)
# copied_dict["names"].append("Jack")
# copied_dict["numbers"].append(6)
 
# print(original_dict)
# print(copied_dict)

# Output:

# {
#     'names': ['Elshad', 'John', 'Edy'], 
#     'numbers': [1, 2, 3, 4, 5]
# }
 
# {
#     'names': ['Elshad', 'John', 'Edy', 'Jack'], 
#     'numbers': [1, 2, 3, 4, 5, 6]
# }


def deep_copy(my_dict):
    new_dict = {}
    for keys, values in my_dict.items():
        # Each value in this dictionary is a list.
        # In this instance, a list is being copied using shallow copy. We are not copying
        # the dictionary. Therefore, shallow copy works in this case.
        new_values = values.copy()
        new_dict[keys] = new_values
    return new_dict    
    
    
original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}
    
copied_dict = deep_copy(original_dict)           
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)        

print(id(original_dict), original_dict)
print(id(copied_dict), copied_dict)