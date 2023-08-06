def password_controller(password):
    if password == "":
        return 'Password cannot be empty'
    else:
        if len(password) >= 8:
            return True
        else:
            return False
        
pwrd = input('Enter password: ')
output = password_controller(pwrd)
print(output)


