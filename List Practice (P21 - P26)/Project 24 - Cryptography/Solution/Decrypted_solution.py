alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


cipher_message = input("Enter your message:\n").upper()
shift_number = int(input("Enter the shift number:\n"))

def decrypt(p_message, p_shift_amount):
  message = ""
  for char in p_message:
    if char in alphabet:
        position = alphabet.index(char)
        old_position = position - p_shift_amount
        while old_position < 0:
            old_position = old_position + 26
        new_letter = alphabet[old_position]
        message += new_letter
    else:
        message += char
  return f"The decoded text is {message}"


print(decrypt(cipher_message, shift_number))