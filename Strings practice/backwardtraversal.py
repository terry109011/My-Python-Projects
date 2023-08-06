user_input = input('Enter a word: ')

def backward_traversal(word):
    l = len(word)
    count = 0
    backward = ''
    while count < l:
        count += 1
        backward += word[-count]
    return backward

while len(user_input) == 0:
    user_input = input('Enter a word: ')
    
print(backward_traversal(user_input))