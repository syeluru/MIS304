# Some basic list operations

def main():
    # Copying lists
    grades = [88.2, 98.6, 96.5, 75.6]
    scores = grades # Copies references
    print (id(grades))
    print (id(scores))

    # Modifying in grades reflects in scores
    grades[2] = 78.5
    print(grades)
    print(scores)

    # Copying lists using list function
    list1 = [2,3,4]
    list2 = list(list1)

    print(list1)
    print(list2)
    print (id(list1))
    print (id(list2))
    # They're different lists now

    # Create a list from a string
    greetings = "hello"
    chars = list(greetings)
    print (greetings)
    print (chars)

    # Create a list by concatenation
    grades2 = []
    print (id(grades2))
    grades2 += grades # Concatenates grades2 and grades
    print (id(grades2))
    # THIS IS DIFFERENT FROM:
    grades2 = grades2 + grades
    # THE ABOVE TWO THINGS ARE DIFFERENT
    # THE SECOND ONE CREATES A NEW OBJECT
    print (grades2)
    print (id(grades2))
    print (grades2 == grades) # True

    # You can repeat with a multiplication
    # but doing a x = x * 3 creates a new object
    # but doing x *= 3 keeps the same object
    # same reasoning as above

    # Concatenate using extend method
    i1 = [2,7,6]
    i2 = [4,5,8]
    i2.extend(i1) # appends all elements of i1 to i2
    print (i1)
    print (i2)

    # List comprehension

    list1 = [x for x in range(10)]
    print (list1)

    list2 = [x * 2.5 for x in list1]
    print(list2)

    list3 = [x for x in list2 if x < 18]
    print(list3)

    list4 = [x for x in list2 if 5.0 < x < 15]
    print (list4)


main()
