# List Addition with Function

# Implement a function which takes two parameters - a list and a value
# and returns new list with value inserted in it without modifying the original list.

# Example

# list1 = [1,2,3,4,5]
# list2 = custom_insert(list1, 6)
# print(list1)
# print(list2)

# Output:
# [1,2,3,4,5]
# [1,2,3,4,5,6]

def custom_insert(a_list, n):
    # Slice method will create a copy of the original list and
    # any change would not affect the original list
    
    # Other method do not create a copy of the original list. 
    # Therefore, new change will affect the original list
    
    new_list = a_list[:]
    new_list.append(n)
    return new_list

list1 = [1,2,3,4,5]
list2 = custom_insert(list1, 6)
print(list1)
print(list2)
 