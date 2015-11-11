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

Chapter 7 = Lists
-lists are kind of like arrays but lists are mutable
-tuple is immutable - these are pretty much arrays

# Notes on 10/21

Basically objects are mutable
A new list will have a new memory allocation,
even if its the same list as before

# Notes on 10/26

Chap 6 Files

Files can be opened for input or output
output to a file from the Program

either text file or binary (binary in the end anyways)
we basically create a variable which references a file object

when you read a line, it automatically adds a '\n' character

# Notes on 11/2

Exception Handling

so far we have been able to do most things without worrying about errors
Types of Errors (not exhaustive):
	ValueError

	IndexError
		-list[3] with only 3 things in the list gives us

We have to catch these errors
"Try and Except" in Python
	-exceptions have to be handled by the programmer
	-typical structure is as follows:
		-try clause/statement (with possible errors)
			statement
			statement
			statement
		-except clause
			-what to do given this error
			-called the exception handler

In OOP, there are always classes and objects
-each data type is an object of the respective class
	-class int, float, etc.
	-Exception is a class too
-an error creates an object of type Exception
	-"throws an exception"

Example:
	class 'SyntaxError'

-we can add an optional else and finally at the end
if nothing is returned, then None is returned
the class of (None) = NoneType

# Notes on 11/4

What happens if an exception is caught/not caught
in a nested function with other functions

When dealing with files, put all the file processing stuff in an else clause
-that way, the else will only be executed if we successfully open the file

START TEST 3

# Notes on 11/11

Procedural Programming (comes under the umbrella of OOP)
-actions and tasks
-variables holding the data and functions manipulating/processing the data
-keep the data and actions separate (goal of procedural programming!)

Object Orientation
-anything and everything is an object
-need a class to create an object
	-class represents a template/prototype/blueprint
-Unified Modeling Language (UML)
	-diagram for a class
	-Each class has a name, and attributes/fields/variables (characteristics, basically)
	-Each class has behaviors/methods that operate on these variables
-Encapsulation
-Example of a Chair class
	-variables:
		-legs, hand, dimensions, etc
	-behaviors:
		-can be moved, picked up, etc.
-Example: Bank Account
	-variables:
		-balance,
	-behaviors:
		-get_balance, add/deposit, remove/withdraw
-We use our blueprint (class) to create objects
-Process of instantiation
	-Creating an object from a class
	ve = ValueError ("some text")
	^thats an instance of the class ValueError

-Data Hiding

-Need a Driver Program/Client/Test Program that actually uses the class, creates an object, etc.
	-when I implement (create) a class, I want to protect my variables.
	-no one should have direct access to my variables. (Data Hiding)

-Example:
	-Die class
	-Attribute:
		-sideUp (what you rolled)
	-Behaviors:
		-getSideUp, rollDie
-define an initializer or Constructor when we define a class

-add two underscores before a variable in a class to make it a private variable
