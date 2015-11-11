# Program to test Die class
import Die #this is the filename so we're just importing a file


def main():
    # Create objects or instances of Die class
    die1 = Die.Die() # FileName.ClassName
    die2 = Die.Die() # Creates the die2 object

    print (die1.getSideUp())
    print (die2.getSideUp())

    # Roll the dice
    die1.roll()
    die2.roll()

    # Roll the dice using a for loop
    for i in range(10):
        die1.roll()
        die2.roll()
        # Display sideup values
        print(die1.getSideUp(), die2.getSideUp())
    #die1.__sideup = 8 # not allowed because private variable
    #die2.__sideup = 10 # same







main()
