# Program to demonstrate a function returning Multiple Values

def main():
    last = ''
    first = ''
    last, first = get_name()

    print (first, last)

def get_name():
    last_name = input("Enter the last name: ")
    first_name = input("Enter the first name: ")

    return last_name, first_name



# Call main
main()
