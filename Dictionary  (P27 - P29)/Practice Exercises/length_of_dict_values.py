# Length of Dictionary Values

# Implement a function which takes a dictionary as a parameter and returns new dictionary.
# In new dictionary the keys remain same but values will be another nested dictionary. 
# Nested dictionary's keys will be values from original dictionary and values will be length
# of values from original dictionary. 

# ---------------------------------------------------------
# Example:
# names_dict = {
#     1 : "Elshad",
#     2 : "Renad",
#     3 : "Johanna",
#     4 : "Appmillers"
# }
# value_length(names_dict)

# ---------------------------------------------------------
# Output:
# {
#     1: {'Elshad': 6}, 
#     2: {'Renad': 5}, 
#     3: {'Johanna': 7}, 
#     4: {'Appmillers': 10}
# }

names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}

# def value_length(my_dict):
#     for key, value in my_dict.items():
#         output_dict = dict()
#         output_dict[value] = len(value)
#         my_dict[key] = output_dict
#     return my_dict

# print(value_length(names_dict))

# Elshad's solution

def value_length_sol(my_dict):
    output_dict = {}
    for key, value in my_dict.items():
        output_dict[key] = {}
        output_dict[key][value] = len(value)
    return output_dict

print(value_length_sol(names_dict))

