# Format List

# Print a given list in the format that is shown below using join method.
# custom_list = [1, 2, 3, 4, 5]

# Output:
# 1 | 2 | 3 | 4 | 5 

custom_list = [1, 2, 3, 4, 5]

# convert int list into a string list
# method 1
list_string = map(str, custom_list)

# convert int list into a string list
# method 2
# string_list = []
# for item in custom_list:
#     string_list.append(str(item))

# join all elements in the list into a string, separated by '|' 
output = ' | '.join(list_string)
print(output)