# Encryption

# Instruction

# Create an encrypt function which takes two parameters : message and shift number. 
# Then inside this function shift each letter of the message forwards in the alphabet 
# by the shift number and return encrypted text.

# Example Input:
# ------------------------------------------------------------
# Do not stop in your storm!
# Shift number = 4
# ------------------------------------------------------------

# Example Output
# ------------------------------------------------------------
# HS RSX WXST MR CSYV WXSVQ!
# ------------------------------------------------------------

import string

def encryption(message, shift_num):
    mess_list = list(message)   # break down message string into a list
    alphabet = list(string.ascii_uppercase)  # create a list of alphabet
    encrypted_list = []  # create a list to appened encrypted message
    for letter in mess_list:
        for letter1 in alphabet:
            if letter == letter1:  # match element in message_list with the index of the same letter in alphabet
                position = alphabet.index(letter1)
                new_position = position + shift_num
                if new_position > 25:
                    new_position = new_position - 26
                encrypted_list.append(alphabet[new_position])
                break
            elif letter == ' ':
                encrypted_list.append(' ')
                break
            elif letter not in alphabet:
                encrypted_list.append(letter)
                break
    encrypted_mess = ''.join(encrypted_list)  # join encrypted_list into an encrypted string
    return encrypted_mess

# ------------------------------------------------------------

# Decryption

def decryption(cipher_message, shift_de):
    mess_list = list(cipher_message)   # break down message string into a list
    alphabet = list(string.ascii_uppercase)  # create a list of alphabet
    decrypted_list = []  # create a list to appened decrypted message
    for letter in mess_list:
        for letter1 in alphabet:
            # match element in message_list with the index of the same letter in alphabet
            if letter == letter1:  
                position = alphabet.index(letter1)
                new_position = position - shift_de
                if new_position < 0:
                    new_position = new_position + 26
                decrypted_list.append(alphabet[new_position])
                break
            elif letter == ' ':
                decrypted_list.append(' ')
                break
            elif letter not in alphabet:
                decrypted_list.append(letter)
                break
    decrypted_mess = ''.join(decrypted_list)  # join encrypted_list into an encrypted string
    return decrypted_mess

# ------------------------------------------------------------

end_program = False
while not end_program:
    
    enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
    if enc_dec == 'E' or enc_dec == 'e':
        my_message = input("Enter your original message:\n").upper()
        shift_num = int(input("Enter the shift number:\n"))
        encrypted_message = encryption(my_message, shift_num)
        print(encrypted_message)
    elif enc_dec == 'D' or enc_dec == 'd':
        my_message = input("Enter your original message:\n").upper()
        shift_num = int(input("Enter the shift number:\n"))
        decrypted_message = decryption(my_message, shift_num)
        print(decrypted_message)
    else:
        print('Incorrect input, please try again!')
        continue
    
    while True:
        restart = input("Type 'Y' to continue. Otherwise, type 'N': ")   
        if restart == 'N' or restart == 'n':
            print('See you later!')
            end_program = True
            break
        elif restart == 'Y' or restart == 'y':
            break
        else: 
            print("Only 'Y' or 'N' allowed. Please try again!")
            continue
    
