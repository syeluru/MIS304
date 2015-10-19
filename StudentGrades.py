# Program to demonstrate nested loops
# This program reads student scores in various courses
# and displays the information

def main():
	# Declare variables
	more_students = "Y"
	total_score = 0.0
	num_passing_grades = 0
	num_failing_grades = 0

	header_line = "%20s%10s%10s%11s%11s"\
	% ("        Name        "," Courses ", " Average  ", \
	"Pass Grades", "Fail Grades")

	detail_line = " "

	# Outer loop - check if there are more students
	while(more_students == 'Y'):
		student_name = input("Enter the student's name: ")
		# Get the number of courses taken 
		num_courses = int(input("Enter the number of courses taken: "))
		# Initialize course count and score total
		course_count = 0
		total_score = 0.0
		# Initialize number of passing and failing grades for the student
		num_passing_grades = 0
		num_failing_grades = 0
		# Initialize average score
		average_score = 0.0

		# Inner loop - for each course taken, get the score
		while (course_count < num_courses):
			# Increment the course counter
			course_count += 1
			# Get the score for the particular course
			score = eval(input("Enter the score for the course %d: " % (course_count)))
			# Increment the total score
			total_score += score

			# Check for passing or failing score
			if (score >= 60.0):
				num_passing_grades += 1
			else: 
				num_failing_grades += 1
			# End of outer loop

		# Compute the average score
		average_score = total_score / num_courses

		# Set the detail line
		detail_line += "%20s%5d%15.2f%11d%11d\n"\
		% (student_name, num_courses, average_score,\
		num_passing_grades, num_failing_grades) 

		# Check if there are more students
		more_students = input("Do you have more students?\
		Press 'Y' or 'N': ")
		# End of the outer loop

	# Print header and detail lines
	print (header_line)
	print (detail_line)

# Call the main function
main()



