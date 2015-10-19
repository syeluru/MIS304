# Program to find min and max

def main():
	# Declare variables
	n1 = 0
	n2 = 0
	n3 = 0
	max = 0
	message = ''

	# Get the user input
	'''n1 = int(input("Enter 1st number: "))
	n2 = int(input("Enter 2nd number: "))
	n3 = int(input("Enter 3rd number: "))
	'''

	n1, n2, n3 = 1, 2, 3
	n1, n2, n3 = eval(input("Enter 3 integers separated by comma: "))
	# Assume n1 is maximum
	max = n1

	if(n1 > max):
		max = n1
	if(n2 > max):
		max = n2
	if(n3 > max):
		max = n3
	# Set the output message
	message = "The maximum of %d, %d, and %d is %d." \
	%(n1, n2, n3, max)

	min = n1
	if(n1 < min):
		min = n1
	if(n2 < min):
		min = n2
	if(n3 < min):
		min = n3

	message += "\nThe minimum of %d, %d, and %d is %d." \
	%(n1, n2, n3, min)
	print(message)

# Run main function
main()