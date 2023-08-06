# Rename Key

# Write a program which renames the key in the dictionary,
# you need to rename key 'city' to 'address' in the following dictionary.

my_dict = {
    "name": "Edy",
    "age":30, 
    "salary": 5000, 
    "city": "London"
}

print(my_dict)
my_dict['address'] = my_dict.pop("city")
print(my_dict)