custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

for element in custom_list:
    if type(element) == int: # or we could write: if isinstance(element, int):
        print(element)