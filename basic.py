# Program to demonstrate basic python statements

print("Welcome to Python Programming")

message = "Welcome to Python Programming!!!"
print (message)
print(type(message))
# message is a variable of type str

number = 25
print (number)
print (type(number))
# number is a variable of type num

price = 12.99
print (price)
print (type(price))

check = True
print (check)
print (type(check))

#List which are mutable
cityList = ['Austin', 'Dallas', 'Chicago']
print (cityList)
print (type(cityList))

#Tuple is immutable
studentList = ('James', 'Lisa')
print (studentList)
print (type(studentList))

print (id(number))
print (id(price))
number = 12.99
print (id(number))
price = 25
print (id(price))