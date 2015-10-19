# Program to print letter grade

def main():
	# Declare variables
	score = 0.0
	grade = ''
	message = ''

	# Get the user input
	score = eval(input("Enter your score: "))
	message = "Youre score is {0:.2f}" .format(score)

	# Determine the letter grade
	'''
	if (score >= 90.0):
		grade = 'A'
	else:
		if (score >= 80.0):
			grade = 'B'
		else:
			if (score >= 70.0):
				grade = 'C'
			else:
				if (score >= 60.0):
					grade = 'D'
				else: 
					grade = 'F'
    '''

	if(score >= 90):
		grade = 'A'
	elif(score >= 80):
		grade = 'B'
	elif(score >= 70):
		grade = 'C'
	elif(score >= 60):
		grade = 'D'
	else: 
		grade = 'F'

	print (message)
	print ("Your letter grade is %s" % grade)

main()