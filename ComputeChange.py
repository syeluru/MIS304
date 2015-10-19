# Program to find dollars and pennies

import tkinter.messagebox

def main():
  # Declare variables 
  amount = int(input("Enter the pennies: "))
  message = ""
  # 1256
  number_of_dollars = amount // 100
  number_of_cents = amount % 100
  #Set the output message
  message = "Amount %d contains %d dollars and %d cents"\
  %(amount, number_of_dollars, number_of_cents)

  print ("Amount", amount, "contains\n",
  "\t", number_of_dollars, "dollars\n",
  "\t", number_of_cents, "cents")
  
  #Display the message
  print(message)
  
  tkinter.messagebox.showwarning("Compute Change", message)
  
  
#Call the main function
main()