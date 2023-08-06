# Concatenate Two Lists in One List Item Wise

# Implement a function which takes two lists as parameter
# and return concatenation of these lists item wise.

# Example:
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# concatenate(list1, list2)

# Output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# ------------------------------------------------------'

list_a = ["Hello", "take", "eat"]
list_b = ["Dear", "Sir"]

def concatenate(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    new_list = []
    for i in range(length1):
        for j in range(length2):
            element = list1[i] + ' ' + list2[j]
            new_list.append(element)
    return new_list

output = concatenate(list_a, list_b)
print(output)