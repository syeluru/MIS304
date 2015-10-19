# Program to check if a given year is a leap year
import tkinter.messagebox

def main():
  # Declare variables with user input
  year = int (input ("Enter year: "))
  message = ""
  isLeapYear = False

  '''
  Year is a leap year if it is divisible by 4 and not divisible by 100 or
  Year is a leap year if it is divisible by 400
  '''
  
  isLeapYear = ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
  if (isLeapYear):
    message =  ("%d is a leap year!" % (year))
    print(message)
  else: 
    message = print ("%d is not a leap year!" % (year))
    print(message)

  tkinter.messagebox.showinfo("Is it a leap year?", message)

main()