# Program to process exceptions

def main():
    try:
        x = int(input("Enter a numerator: "))
        y = int(input("Enter a denominator: "))
        result = x/y

    except SyntaxError:
        print("Please separate the numbers by a comma, and not a space.")
    except ZeroDivisionError:
        print ("Please enter a nonzero denominator.")
    except ValueError:
        print ("Please enter numeric values")
    # This is like an open bucket where any other error is caught
    except Exception as ex:
        print (type(ex))
        print("%s error occurred." %(ex))
    else:
        print ("Everything looks good. This is the else clause.")
        # Basically when no error happens
        print ("Result:", result)
    finally:
        print ("I'm in the finally clause.")
        print ("I will be processed no matter what.")
        print (result)


# Call main
main()
