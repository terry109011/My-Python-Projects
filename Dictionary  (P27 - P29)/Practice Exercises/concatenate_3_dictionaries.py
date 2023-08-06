# Concatenate three dictionaries

# Implement a function which takes three dictionaries as parameters and
# concatenate them into one new dictionary without updating the current
# ones and returns new dictionary with all elements of these three dictionaries in it.

# Hint : use update() method of dictionary.

dict_a={1: "one", 2: "two"}
dict_b={3: "three", 4: "four"}
dict_c={5: "five", 6: "six"}

def concatenate_dict(d1, d2, d3):
    output_dict = {}
    for dic in [d1, d2, d3]:
        output_dict.update(dic)
    return output_dict

print(concatenate_dict(dict_a, dict_b, dict_c))