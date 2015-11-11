# Program to compute averages sales per week

def main():
    sales_id = 0
    average_sales = 0

    infile = open("sales.txt", 'r')
    outfile = open("weeklyavgsales.txt", 'w')
    # Print the header

    # Loop through the weeks and build a list of
    # sales for each week
    weekly_sales = []
    for wk in range(1,13):
        total_sales = 0
        line = infile.readline()
        while (line != ''):
            sales_list = line.split()
            weekly_sales.append(sales_list[wk])
            # Read next line
            line = infile.readline()

        # Loop through the weekly_sales list
        # Compute total and average
        for sales in weekly_sales:
            total_sales += int(sales)

        average_sales = total_sales/len(weekly_sales)

        # Display output
        output = ("%2d %10d %12.2f" % (wk, total_sales, average_sales))
        print (output)
        outfile.write(output + "\n")

        # Reset the variables
        weekly_sales = []
        total_sales = 0
        average_sales = 0.0
        infile.seek(0)

    infile.close()
    outfile.close()

# Call main
main()
