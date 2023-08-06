def count_letter(word, letter):
    word_len = len(word)
    word = word.lower()
    letter = letter.lower()
    count = 0
    if word_len == 0:
        quit
    else:
        for char in word:
            if char == letter:
                count += 1
    return count

user_input = input('Enter a word: ')
letter_chosen = input('Enter a letter: ')
times = count_letter(user_input, letter_chosen)
print(f"The letter '{letter_chosen}' appears {times} times in '{user_input}'.")


    