#program to compute area
"""
length = 20
width = 5
area = length * width

print (type(length))
print (type(width))

print (area)
print (type(area))

length = 12.8
width = 5.6

area = length * width
print (type(area))
print (area)

#f is format specifier for floating numbers
#.2 is two decimal places
print ("Area = %.3f" %(area))

print ("Area =", format(area, '.2f'))
print( "Area of rectangle = {}" .format(area))
#{} acts as a placeholder
print ("Area of rectangle = {0:.2f}" .format(area))
print ("{0:.2f} is the area of the rectangle" .format(area))

print ("Area of rectangle with length {0:.2f} \
and width {1:.2f} is {2:.2f}\
" .format(length,width,area))

"""
'''
#Find the area with user input
length = int(input ("Enter the length: "))
width = int(input ("Enter the width: "))

print (type(length))
print (type(width))

#l = int(length)
#w = int(width)

area = length * width
print (area)

#Find the area of a circle
# Get the user input
radius = float(input ("Enter the radius: "))
circleArea = 3.14159 * radius * radius

print (circleArea)
print ("Area of circle with radius %.2f \
is %.2f" %(radius, circleArea))
'''

def find_area(length, width): #these are parameters

    area = length * width
    return(area)
    # void function because no values are returned (only printed)

def display_message(message):
    print(message)

def main():
    length = 0.0
    width = 0.0
    area = 0.0
    message = ''

    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    #Call a function to compute area
    area = find_area(length, width)

    message = "Area of rectangle: %.2f" %area
    #print (message)
    display_message(message)
main()
