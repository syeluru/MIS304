# Program to compute the average of given numbers

def main():
	# Declare variables
	number = 0.0
	total = 0.0
	count = 0
	message = ''

	# Get the user input
	number = eval(input("Enter a number (or zero to quit): ")

	# Repeatedly get the user input and add them up
	while(number > 0.0):
		# total = total + number
		total += number
		count += 1
		number = eval(input("Enter the next number (or zero to quit): "))

	# Set the message
	if(count > 0):
		average = total / count
		message = 'Average of %d numbers is %.2f'\
		% (count,average)

	# Display the message
	print(message)

# Call main function
main()
