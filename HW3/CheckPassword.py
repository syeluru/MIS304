# Program to verify the password
def checkPassword(password):
    # Length
    valid_length = False
    if len(password) >= 8:
        valid_length = True
    # Contains two digits
    num_digits = 0
    valid_digits = False
    for i in range(len(password)):
        if password[i].isdigit():
            num_digits += 1
    if num_digits >= 2:
        valid_digits = True
    # Contains an uppercase letters\
    contains_upper = False
    for i in range(len(password)):
        if password[i].isupper():
            contains_upper = True
    # Contains a lowercase letter
    contains_lower = False
    for i in range(len(password)):
        if password[i].islower():
            contains_lower = True
    # Contains a special character
    test_chars = ['!','@','#','$','%','^','&','*','(',')']
    contains_special_char = False
    for i in range(len(password)):
        for j in range(len(test_chars)):
            if password[i] == test_chars[j]:
                contains_special_char = True
    return (valid_length and valid_digits and contains_upper and contains_lower and contains_special_char)

def main():
    user_pass = input("Enter your password: ")
    if checkPassword(user_pass):
        valid = 'valid'
    else:
        valid = 'invalid'
    print ("The password you entered is %s" % valid)

main()
