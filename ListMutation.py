# Program list mutation

def main():
    list_x = [1,2,3]
    print("list_x", list_x)
    print("ID of list_x: ", id(list_x))

    list_y = [1,2,3]
    print("list_y", list_y)
    print("ID of list_y: ", id(list_y))

    print("Mutate list_x")
    list_x[1] = 5
    print("list_x", list_x)
    print("ID of list_x: ", id(list_x))

    #Assign a new list to list_x
    list_x = [7,8,9] #Creates a new object
    print("list_x", list_x)
    print("ID of list_x: ", id(list_x))
main()
