# Create a List from Two Lists

# Given two lists create a third list by picking an 
# odd-index element from the first list and even-index
# elements from the second.

# list_one = [4, 12, 16, 21, 24, 28, 32]
# list_two = [5, 10, 15, 20, 25, 30, 35]

# Output
# [12, 21, 28, 5, 15, 25, 35]

list1 = [4, 12, 16, 21, 24, 28, 32]
list2 = [5, 10, 15, 20, 25, 30, 35]

list3 = list1[1::2] + list2[0::2]

print(list3)