''' Program to determine which salesperson had the maximum sales
given 5 sets of salesperson and sales numbers'''

# Imports the necessary module for tkinter
import tkinter.messagebox

def main():
  	# Creates an empty lists  for which to input sales ID and sales info
	salespersons = []
	sales = []
	# Creates a for loop to gather user input 5 times
	for i in range(1,6):
		# Command to gather the user input
		sales_input = input("Enter sales person ID and units sold (both integers): ")

		# Code to get the actual sales ID and sales value from each input
		temp_list = sales_input.split(',')
		sales_point = [int(x) for x in temp_list]

		# Appends into a list to gather all the various points
		salespersons.append(sales_point[0])
		sales.append(sales_point[1])

	# Gets the max of the sales by using the max command
	max_sales = max(sales)
	# Gets the index of the max sales so we can get the corresponding seller
	sales_index = sales.index(max_sales)
	# Gets the ID of the corresponding seller with the max sales
	max_seller_ID = salespersons[sales_index]

	# Displays in message box the necessary message
	tkinter.messagebox.showinfo("Maximum Sales", "Maximum units sold: %d\
	\nWinning sales person: %d" % (max_sales, max_seller_ID))

main()