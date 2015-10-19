# Program to convert given temperature into either celsius or fahrenheit

# Imports the necessary module
import tkinter.messagebox

def main():
  print ("Welcome to Temperature Conversion Program\n")
  
  print ("1) Convert from Fahrenheit to Celsius")
  print ("2) Convert from Celsius to Fahrenheit \n")
  
  # Determines which scale to convert from
  choice = int(input("Enter your choice: "))
    
  # Gathers user input and converts to integer
  temp_to_convert = float(input("Enter the temperature to convert: "))
  
  # If statement to determine which formula to use
  if (choice == 1):
    input_temp_type = "Fahrenheit"
    final_temp = (5.0/9.0) * (temp_to_convert - 32)
    final_temp_type = "Celsius"
  elif (choice == 2):
    input_temp_type = "Celsius"
    final_temp = (9.0/5.0) * temp_to_convert + 32
    final_temp_type = "Fahrenheit"

  
  # Displays in messagebox wit format characters to simplify
  tkinter.messagebox.showinfo("Temperature Conversion", "You selected option %d\
  \n%.2f degrees %s is equal to %.2f degrees %s"\
  % (choice, temp_to_convert, input_temp_type, final_temp, final_temp_type))

main()