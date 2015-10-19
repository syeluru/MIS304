# Program to demonstrate passing arguments

def main():
    x = 5
    print ("Inside the main function: ")
    print ("\tBefore calling square: ")
    print ("\t\tValue of x:", x)
    print ("\t\tAddress of x:", id(x))

    square(x)

    print ("Inside the main function: ")
    print ("\tAfter calling square: ")
    print ("\t\tValue of x:", x)
    print ("\t\tAddress of x:", id(x))

def square(y):
    print("Inside square function: ")
    print("\tBefore updating y: ")
    print("\t\tValue of y:", y)
    print("\t\tAddress of y:", id(y))

    # Update y
    y = y ** 2

    print("Inside square function: ")
    print("\tBefore after y: ")
    print("\t\tValue of y:", y)
    print("\t\tAddress of y:", id(y))


# Call main
main()
