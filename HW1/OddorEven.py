# Program to determine whether a given number is odd or even.

# Imports the necessary module for tkinter
import tkinter.messagebox

def main():
  #Gets the input from user and stores in valuable number
  number = int(input("Enter the number: "))
  
  #Checks to see if number is odd or even
  if (number % 2 == 0):
    tkinter.messagebox.showinfo("Even or Odd", "Number %d is an Even number" % number)
  else:
    tkinter.messagebox.showinfo("Even or Odd", "Number %d is an Odd number" % number)

main()