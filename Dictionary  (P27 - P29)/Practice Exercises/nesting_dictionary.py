# Nesting Dictionary Exercise

# Implement a function that adds new key value pairs to the programming_language list.
# You can see the list below in which there is only two dictionaries, after insert method,
# there should be three dictionaries. After insertion we need to print programming_language
# list to the console.

# -------------------------------------------------------------------------------------------
# programming_language = [
#     {"user_name" : "Elshad",
#      "favorite_languages" : ["Python", "Java", "C#"],
#      "experience": 10 
#     },
#     {"user_name":"Renad",
#      "favorite_languages" : ["Scratch","Python"],
#      "experience" : 2
#     },
# ]

# -------------------------------------------------------------------------------------------
# Example:
# add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10)

# -------------------------------------------------------------------------------------------
# Output:
# [
#  {'user_name': 'Elshad', 
#   'favorite_languages': ['Python', 'Java', 'C#'], 
#   'experience': 10
#  },
#  {'user_name': 'Renad', 
#   'favorite_languages': ['Scratch', 'Python'], 
#   'experience': 2
#  },
#  {'user_name': 'Edy', 
#   'favorite_languages': ['Java', 'Kotlin', 'Swift'], 
#   'experience': 10
#  }
# ] 

import pprint

global programming_language

programming_language = [
    {"user_name" : "Elshad",
     "favorite_languages" : ["Python", "Java", "C#"],
     "experience": 10 
    },
    {"user_name":"Renad",
     "favorite_languages" : ["Scratch","Python"],
     "experience" : 2
    }
]

pprint.pprint(programming_language)

def add_new_user(name, prog_language_list, exp):
    # make a new dictionary
    new_user = dict()
    new_user["user_name"] = name
    new_user["favourite_languages"] = prog_language_list
    new_user["experience"] = exp
    # append new dictionary to "programming_language" list
    programming_language.append(new_user)
    pprint.pprint(programming_language)

print("\n")
print("Appended list:")
add_new_user('Edy', ['Java', 'Kotlin', 'Swift'], 10)



