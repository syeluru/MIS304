# Exception Chaining

def main():
    y = 3
    try:
        x = 2
        y = x + y
        fun1() #function 1
    except SyntaxError as se:
        print(se)
    finally:
        print ("Finally, I'm in main")


    print("x =", x)
    print('y =', y)
    print("End of function main")

def fun1():
    try:
        fun2() # Call to function 2
    except IndexError as ie:
        print(str(ie) + ' booyah')
    finally:
        print("Finally, I'm in function 1")

    print ("End of function 1")

def fun2():
    try:
        fun3() # Call function 3
    except ValueError as ve:
        print(ve)
    finally:
        print("Finally, I'm in function 2")

    print("End of function 2")

def fun3():
    try:
        #ex = ZeroDivisionError ("ZeroDivisionError in function 3")
        #raise ex
        #ex = ValueError("ValueError in function 3")
        #raise ex
        ex = IndexError ("IndexError in function 3")
        raise ex
        #ex = SyntaxError ('SyntaxError in function 3')
        #raise ex
        #ex = TypeError ("TypeError in function 3")
        #raise ex
        # Caught in the same function
    except ZeroDivisionError:
        print("ZeroDivisionError caught in function 3")

    finally:
        print("Finally, I'm in function 3")

    print ("End of function 3")

main()
