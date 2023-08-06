import string

def refactor_position(shifted_position, cipher_type):
    if cipher_type == 'E' or cipher_type == 'e':
        while shifted_position > 25:
            shifted_position = shifted_position - 26   
        return shifted_position
    elif cipher_type == 'D' or cipher_type == 'd':
        while shifted_position < 0:
            shifted_position = shifted_position + 26
        return shifted_position
    
    
    
def cipher(original_message, shift_num, cipher_type):
    alphabet = list(string.ascii_uppercase)
    new_message = ""
    if cipher_type == 'D' or cipher_type == 'd':
        shift_num *= -1
    for char in original_message:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = current_position + shift_num
            new_position = refactor_position(new_position, cipher_type)
            new_message += alphabet[new_position]
        else:
            new_message += char
    print(f"Here is the {'decode' if (cipher_type == 'D') or (cipher_type == 'd') else 'encode'}d result: {new_message}")
    return new_message

from logo import logo
print(logo)


exit = False
while not exit:
    # Prompt user's input
    enc_dec = input("Type 'E' for encode, type 'D' for decode:\n")
    if enc_dec == 'E' or enc_dec == 'e' or enc_dec == 'D' or enc_dec == 'd':
        initial_text = input('Enter the message: ').upper()
        while True:
            try:
                shift_amount = int(input('Enter shift number: '))
                break
            except ValueError:
                print('Numeric input only, please try again!')
                continue
        cipher(original_message = initial_text, shift_num = shift_amount, cipher_type = enc_dec)
    else:
        print('Incorrect input, please try again!')
        continue
    
    # Exit or Continue
    while True:
        restart = input("Type 'Y' to continue. Otherwise, type 'N': ")
        if restart == 'N' or restart == 'n':
            print('See you later!')
            exit = True
            break
        elif restart == 'Y' or 'y':
            break
        else: 
            print('Incorrect input. Try again!')
            continue
    
    