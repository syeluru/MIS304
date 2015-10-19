# Program to determine the number of years it takes to double an investment

def main():
	#Declare variables
	initial_amount = 0
	target_amount = 0.0
	rate_of_interest = 0.0
	years = 0
	balance = 0.0

	# Get the user input
	initial_amount = eval(input("Enter the initial amount: "))
	rate_of_interest = eval(input("Enter the rate of interest (e.g., 5,75): "))

	target_amount = 2.0 * initial_amount
	balance = initial_amount

	while (balance < target_amount):
		years += 1
		interest_amount = balance * rate_of_interest/100
		balance += interest_amount
		print("%d: %.2f, %.2f" % (years, interest_amount, balance))

	# Set the output message
	message = "The investment of %.2f doubles in %d years "\
	%(initial_amount, years)

	print (message)
	
#Call main function
main()
