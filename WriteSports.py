# program to create a text file

def main():
    # Open a file for output/writing
    outfile = open("sports.txt", "w")

    # Process
    # Add or write records to the file
    outfile.write("Football\n")
    outfile.write("Baseball\n")
    outfile.write("Tennis")

    # Close the output file
    outfile.close()



# Call main
main()
