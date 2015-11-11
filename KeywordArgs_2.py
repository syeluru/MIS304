#Program to demonstrate keyword arguments


def main():

	principal = 10000.0
	rate = 0.05
	periods = 10
	#Positional arguments
	calculateInterest(10000.0, 0.05, 10)
	
	calculateInterest(principal, rate, periods)
	
	#Keyword arugments
	calculateInterest(rate=0.25, periods=12, principal=12000.0)
	
	#Mixing Keywords and Positional arguments
	calculateInterest(10000.0, periods=10, rate=0.05)
	
	#Error because positional argument comes after
	#Keyword argument
	calculateInterest(10000.0, rate=0.01, 10)
	


def calculateInterest(principal, rate, periods):

	interest = principal * rate * periods
	print("Simple interest is $",\
	format(interest, '.2f'))


#Call main
main()


