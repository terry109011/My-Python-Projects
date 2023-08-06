def first_last_characters(word):
    word_len = len(word)
    output = ''
    if word_len < 4:
        return ''
    else:
        first_two_char = word[0:2]
        last_two_char = word[-2:]
        output = first_two_char + last_two_char
    return output

user_input = input('Enter a word: ')
result = first_last_characters(user_input)
print(result)