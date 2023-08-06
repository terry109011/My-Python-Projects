# Remove and Add
# Remove an element at index 4 in a given
# list and add it to the 2nd position and
# at the end of the list.

# custom_list = [10, 44, 57, 99, 11, 33, 84]

# Output:
# [10, 44, 11, 57, 99, 33, 84, 11]
# ------------------------------------------

custom_list = [10, 44, 57, 99, 11, 33, 84]

# pop element at index 4 and store it in a variable
new_num = custom_list.pop(4)
print(custom_list)

# insert element in 2nd index and at the end of list
custom_list.insert(2, new_num)
custom_list.append(new_num)

print(custom_list)