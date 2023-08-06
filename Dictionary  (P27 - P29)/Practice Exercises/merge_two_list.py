# Merge Two Dictionary

# Implement a function which takes as parameter two dictionaries 
# and merge these two dictionaries using Dictionary methods into
# third dictionary.

# No loop allowed

def merge_dict(p_dict1, p_dict2):
    # shallow copy of dict 1
    dict3 = p_dict1.copy()
    dict3.update(p_dict2)
    return dict3

dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}
print(merge_dict(dict1, dict2))

