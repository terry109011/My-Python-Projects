# My Solution
# def count_character(my_string):
#     my_string.upper()
#     output_dict = dict()
#     already_counted = []
#     for letter in my_string:
#         if letter in already_counted:
#             continue
#         count = 0 
#         for i in range(1, len(my_string) + 1): 
#             if letter == my_string[i - 1]:
#                 count += 1
#         output_dict[letter] = count
#         already_counted += letter
#     return output_dict

# print(count_character("MYNAMEISTERRY"))

# -----------------------------------------------------
# Elshad's Solution
def count_character_sol(my_string):
    output_dict = dict()
    for character in my_string:
        if character not in output_dict:
            output_dict[character] = 1
        else:
            output_dict[character] += 1
    return output_dict

print(count_character_sol("MYNAMEISTERRY"))



        