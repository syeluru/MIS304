# Program to read sports.txt and process the records

def main():
    infile = open("sports.txt", 'r')
    '''
    file_contents = infile.read()
    # that reads all the contents

    print (file_contents)
    '''



    # Read a specific number of characters
    s1 = infile.read(4)
    print(s1)
    s2 = infile.read(10)
    print (s2)


    infile.close()

    infile = open("sports.txt", 'r')

    #This time using the readline method
    print("Read records using readline() method")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    print (repr(line1))
    print (line2, end='')
    print (line3, end='')
    print (line4)

    infile.close()
    infile = open("sports.txt", 'r')

    # Readlines method puts the data into a lists
    # Each line becomes an element of the list
    sports_list = infile.readlines()

    print (sports_list)
    infile.close()
main()
