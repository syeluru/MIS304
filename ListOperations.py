#More list operations

def main():
    employees = []
    print (employees)
    print (id(employees))
    employees.append("James") # Add an element to the list
    employees.append("Emily") # Add another element
    print (employees)
    print (id(employees))

    # You can index
    # You can do like a if x in list, then blank
    # You can insert into a list
    employees.insert(1, "Tom")
    print(employees)

    # To find an element that occurs again
    # Speciy a starting position for the search and then add 1


main()
