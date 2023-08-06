# Implement a function which takes the string type list 
# as a parameter and returns the count of the number of 
# strings where the string length is 2 or more and the 
# first and the last characters are same.

# Example:

# list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
# count_words(list1)

# Output
# 3
# ---------------------------------------------------

def count_words(p_list):
    count = 0
    # traverse through the list
    for word in p_list:
        # check element length
        if len(word) < 2:
            pass
        else:        
        # check if the first and last letter match
            if word[0] == word[-1]:
                count += 1
    return count

# ---------------------------------------------------
# Second solution
# def count_words(p_list):
#     count = 0
#     # traverse through the list
#     for word in p_list:
#         if len(word) >= 2 and word[0] == word[-1:]
#                 count += 1
#     return count
#---------------------------------------------------

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc','xx','yy']
print(count_words(list1))