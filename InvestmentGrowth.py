# Program to print growth of a investment

def main():
	# Declare variables
	deposit_amount = 0.0
	rate_of_interest = 0.0
	number_of_years = 0

	# Get the user input
	deposit_amount, rate_of_interest, number_of_years = eval(input("Enter the deposite amount, interest rate, and number of years: "))

	# Add a header line to make it look nicer

	# Print a table of balances for each year
	balance_amount = deposit_amount
	for year in range(1, number_of_years + 1):
		interest_amount = balance_amount * rate_of_interest/100
		balance_amount += interest_amount
		print ("%4d%10.2f" % (year,balance_amount))

	print()



main()