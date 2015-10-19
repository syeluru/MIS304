# Result = 0
# num = 452
# we want 254

# Program to check whether a number is a palindrome

def main():
    # Declare variables
    number = 0
    message = ''
    reverse_number = 0

    # Get the user input
    number = int(input("Enter an integer: "))

    # Call reverse function
    reverse_number = reverse(number)
    if reverse_number == number:
        display_message(reverse_number)
    else:
        print ("The number %d is not a palindrome." % number)

def display_message(message):
    print (message)

def reverse(num):
    result = 0
    while (num != 0):
        remainder = num % 10
        result = result * 10 + remainder
        num = num // 10
    return (result)



main()
