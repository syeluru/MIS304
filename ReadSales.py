# Program to compute average sales per week
# For each sales_person

def main():
    # Define variables
    sales_id = 0
    average_sales = 0.0

    # Open the file for input/reading
    infile = open("sales.txt", 'r')


    # Open a file for output/writing
    outfile = open("salesaverages.txt", 'w')

    # Print the header
    header = ("%s %s" % ("Sales ID", "Average Sales"))
    print (header)
    outfile.write(header + "\n")

    for line in infile:
        total_sales = 0.0
        # Convert data in each line into a list
        sales_list = line.split()
        sales_id = sales_list[0]
        sales_count = len(sales_list) - 1

        # Compute the total sales for 12 weeks
        for i in range(1,sales_count + 1):
            total_sales += int(sales_list[i])

        # Compute average sales
        average_sales = total_sales / sales_count

        # Display output
        print ("%6s %12.2f" %(sales_id, average_sales))

        outline = "{0:6s}{1:s}{2:12.2f}{3:s}".format(sales_id, ' ', average_sales, "\n")
        outfile.write(outline)


    # Close the input file
    infile.close()

    # Close the output file
    outfile.close()




main()
