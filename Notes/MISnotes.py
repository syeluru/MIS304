# Python Notes on 8/31

Print(" ---- ")
^a python function

The text we pass inside is called a string literal
Instead, we can use a string variable
Example: message = "Welcome to Python Programming!!!"
(message is a string variable with the string above)

-every variable has a type
	-string, int, float, boolean
	-the variable only points to a memory location that has the string value
	-it itself does not contain the value string

List (like arrays but mutable)
Tuple (immutable list)

Don't use camelCase
Use city_list

String and numeric literals (when you are not using a variable)


# Python Notes on 9/9


Library
  Modules (basically like programs)
    functions
    Variables

    -any programming language comes with a standard library
     that comes with predefined functions, etc.
    -main() is the starting point for any software application
    	-so in python, write the main() first


Control Structures

Sequence Structure => (one thing after another)
Decision/Selection Structure => where you execute certain statements based on a certain condition
	-usually checked with an if statement
	-then the rest of the code continues
Dual Selection Structure => if something else something


# Python Notes on 9/14

Multiple Selection Structure
	-nested structure essentially
  -if true, then (if true this if false this)
  -each conditional has a subsequent conditional after it

  -eval method is a function that essentially interprets a string as code


# Python Notes on 9/16

Loops, Iterations, Repetitive Structures
-two types: while or for

while loop:
  -the condition should be dynamic so the loop stops at some point
  -otherwise it becomes an infinite loop

# Python Notes on 9/21

Nested Loops

Outer loop
  -inner Loop
    -inner conditional that then checks back with the inner loop
    -once inner loop fails, then outer loop

# Python Notes on 9/23

Sentinel value terminates the Sequence

For loop
for i in something:
  code in the loop

Step value when you want to increment by something other than 1
like for i in range (0, 10, 2):
  print (i)

the 2 would be the step value
step value can also be negative


if you have a %-10s it will left justify but by default its right justified

# Python Notes on 9/28

Function = group/set of statements
Advantages:
1) Modularity
2) Easy Maintenance
3) Reuse
4) Faster Design
5) Quick Testing

Two Types:
-Void Function
-Value Returning Function

all functions start with def
def main(): # for example

but we can def any other function
def function():
    #statements

we can call other functions within main
(so call main last)

Scope of a variable
-local variable
    -limited to main if a variable is defined within main #for example

In Python, everything is an object
-once an object is created, its immutable

# Notes on 10/7

With keyword arguments, there is no 1 to 1 correspondence
It is keyword based
so if we had
def hello(world, not_world):
	blah

we can do
hello(not_world = 'world', world='not_world')
(so the order doesnt have to be the same)

You can also mix positional and keyword arguments
	-the positional one has to be in the right place basically

Void vs. Value-Returning functions
	basically if there is a return function, then it is value-returning

Global vs. local variables
	-global variables are defined outside all the functions
	-global variables can be changed inside functions, however
	-so not advisable to use them
	-declare with capital letters if its a constant
	CONTRIBUTION_RATE = 0.05 (outside of any functions)

#Notes on 10/14

a = "I like eating pie"
a[::3] does the whole string in increments of 3
so I + i + "" + t + g

def main():
	quote = "A balanced diet means a cupcake in each hand"
	if 'diet' in quote:
		print (True)
	else:
		print (False)

	if 'Cupcake' not in quote:
		print ("True")
	else:
		print ("False")

	'''or'''

	print ('cupcake' not in quote)

	digit = '63826'
	if digit.isdigit():
		print("True")
	else:
		print("False")

	alpha = "Holiday"
	if alpha.isalpha():
		print("True")
	else:
		print('False')

s = '\t Austin \t'
print (repr(s))
^prints the hidden white space characters too

you can lstrip, rstrip, strip, or strip('\t')
to strip something in particular

# Notes on 10/19
# Program string searching

def main():
  s1 = "justification"
  s1.endswith("str") method
  s1.startswith("str") method
  s1.find("str") # starting position of "str"
  s1.count("t")) # how many times t appears
  returns a -1 in the event of no such string found
