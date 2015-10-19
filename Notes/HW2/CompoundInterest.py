# Program to compute compound interest


import math
import tkinter.messagebox



def main():
    a = 1000 #Initial amount
    n = 10 #Number of years
    r = 5 #first rate of interest
    final_message = ''
    final_message += print_header_line() + '\n'
    line = "----------"
    final_message += "----%12s%12s%12s%12s%12s%12s\n\n" % (line, line, line, line, line, line)
    for year in range(1,11):
        message_header = "%4d" % year
        message = ''
        for rate in range(5,11):
            amount = a * math.pow((1.0 + rate/100), year)
            message += ('%12.2f' % amount)

        final_message += message_header + message + '\n'
    print (final_message)
    tkinter.messagebox.showinfo("Compound Interest", final_message)

def print_header_line():
    message = "Year"
    for rate in range(5,11):
        amount_header = "Amount<%d%%>" % rate
        message += "%12s" % amount_header
    return (message)


main()
