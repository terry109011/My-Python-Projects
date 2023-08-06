# Step 1 - Create a sentence maker function
# Step 2 - Create a loop which asks input from a user continuously
# Step 3 - Combine everything together

def sentence_maker(p_input):
    question_word = ['How', 'What', 'When', 'Where', 'Why']
    my_list = p_input.split()
    if my_list[0] in question_word:
        output_str = p_input + '?'
    else:
        output_str = p_input + '.'
    return output_str
    
story = ""
while True:
    user_input = input('What is on your mind? ').capitalize()
    if user_input == '\end':
        break
    else:
        my_answer = sentence_maker(user_input)
    story += my_answer + ' '
    
    
print(story)  
    