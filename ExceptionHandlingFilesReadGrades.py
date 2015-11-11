# Exception Handling when using files

def main():
    file_name = input("Enter the input file name: ")
    try:
        infile = open(file_name, 'r')
        #getConnection()
    except FileNotFoundError as fnfe:
        #print (fnfe)
        print ("Input file not found")
    else:
        try:
            print("Read input file")
            print ("Process data")
        except Exception as ex:
            print ("Something went wrong")
        else:
            print ("Everything is good")
            print ("Display the output")
        finally:
            infile.close()
    finally:
        print ("Finally, I'm in main")

main()
