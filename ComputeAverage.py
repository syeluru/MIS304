# Program to compute average

n1 = int (input ("Enter 1st number: "))
n2 = int (input ("Enter 2nd number: "))
n3 = int (input ("Enter 3rd number: "))
#the things on the right above are called expressions
# "=" is an assignment operator

avg_float = (n1 + n2 + n3)/3
avg_int = (n1 + n2 + n3)//3

print (avg_int)
print (avg_float)

print ("Average of {0:d}, {1:d}, and {2:d} is {3:.2f}"\
.format(n1, n2, n3, avg_float))
