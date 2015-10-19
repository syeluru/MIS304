# Program to print a power table
def main():
    x = int(input("Enter the number of x values: "))
    y = int(input("Enter the number of y values: "))
    power_table(y,x)

def power_table(y_max, x_values):
    # Print the header lines
    for y in range(1,y_max + 1):
        print ("%10d" %(y), end = '')
    print()

    for y in range(1,y_max + 1):
        print ("%10s" %("x "), end = '')
    print()

    #Print the table body
    for x in range(1,x_values+1):
        for y in range(1,y_max+1):
            print ("%10d" %x**y, end='')
        print()



main()





'''
1    2    3
x    x    x
1    1    1
2    4    8
3    9    27
'''
