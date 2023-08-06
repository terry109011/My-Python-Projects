def sentence_maker(text):
    question_words = ['How', 'What', 'When', 'Where', 'Why']
    capitalised_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return "{}?".format(capitalised_text)
    return "{}.".format(capitalised_text)

result = []
while True:
    user_input = input('What is on your mind? ')
    if user_input == "\end":
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)
        
story = " ".join(result)
print(story)