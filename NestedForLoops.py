# Program to demonstrate nested for loops

def main():
	for i in range(10):
		for j in range(10):
			print ("*", end = " ")
		print()

	for i in range(10):
		print ("* " * i)
	print ()

	for i in range(10):
		for j in range(i):
			print ("*", end = ' ')
		print ()

	# print multiplication table
	for row in range(1, 11):
		for col in range(1, 11):
			print ("%4d" % (row * col), end = ' ')
		print ()


main()