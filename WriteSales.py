# Given a file with sales ID as the first in each row
# and then find averages of rows as well as columns

# Program to create sales Files
from random import randint

def main():
    # Open the file for output
    outfile = open("sales.txt", 'w')
    for sp in range(10):
        sales_person = str(randint(1001, 2000))
        outfile.write(sales_person + " ")
        # Generate sales figures for 12 weeks
        for sales in range (12):
            number = randint(10,50)
            number_str = str(number)
            outfile.write(number_str + " ")
        outfile.write("\n")

    # Close the output file
    outfile.close()

main()
