#Program to display income tax

import tkinter.messagebox

def tax_1(income):
    # Tax Bracket for 1
    if income >= 0 and income <= 8350:
        return income * 0.1
    elif income > 8350 and income <= 33950:
        return ((income - 8350) * 0.15 + 8350 * 0.1)
    elif income > 33950 and income <= 82250:
        return ((income - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
    elif income > 82250 and income <= 171550:
        return ((income - 82250) * 0.33 + (82250 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
    elif income > 171550 and income <= 372950:
        return ((income - 171550) * 0.33 + (171550 - 82250) * 0.33 + (82250 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
    elif income > 372950:
        return ((income - 372950) * 0.35 + (372950 - 171550) * 0.33 + (171550 - 82250) * 0.33 + (82250 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
def tax_2(income):
    # Tax Bracket for 2
    if income >= 0 and income <= 16700:
        return income * 0.1
    elif income > 16700 and income <= 67900:
        return ((income - 16700) * 0.15 + 16700 * 0.1)
    elif income > 67900 and income <= 137050:
        return ((income - 67900) * 0.25 + (67900 - 16700) * 0.15 + 16700 * 0.1)
    elif income > 137050 and income <= 208850:
        return ((income - 137050) * 0.33 + (137050 - 67900) * 0.25 + (67900 - 16700) * 0.15 + 16700 * 0.1)
    elif income > 208850 and income <= 372950:
        return ((income - 208850) * 0.33 + (208850 - 137050) * 0.33 + (137050 - 67900) * 0.25 + (67900 - 16700) * 0.15 + 16700 * 0.1)
    elif income > 372950:
        return ((income - 372950) * 0.35 + (372950 - 208850) * 0.33 + (208850 - 137050) * 0.33 + (137050 - 67900) * 0.25 + (67900 - 16700) * 0.15 + 16700 * 0.1)
def tax_3(income):
    # Tax Bracket for 3
    if income >= 0 and income <= 8350:
        return income * 0.1
    elif income > 8350 and income <= 33950:
        return ((income - 8350) * 0.15 + 8350 * 0.1)
    elif income > 33950 and income <= 68525:
        return ((income - 33950) * 0.25 + (68525 - 33950) * 0.15 + 8350 * 0.1)
    elif income > 68525 and income <= 104425:
        return ((income - 68525) * 0.33 + (68525 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
    elif income > 104425 and income <= 186475:
        return ((income - 104425) * 0.33 + (104425 - 68525) * 0.33 + (68525 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
    elif income > 186475:
        return ((income - 186475) * 0.35 + (186475 - 104426) * 0.33 + (104426 - 68525) * 0.33 + (68525 - 33950) * 0.25 + (33950 - 8350) * 0.15 + 8350 * 0.1)
def tax_4(income):
    # Tax Bracket for 4
    if income >= 0 and income <= 11950:
        return income * 0.1
    elif income > 11950 and income <= 45500:
        return ((income - 11950) * 0.15 + 11950 * 0.1)
    elif income > 45500 and income <= 117450:
        return ((income - 45500) * 0.25 + (45500 - 11950) * 0.15 + 11950 * 0.1)
    elif income > 117450 and income <= 190200:
        return ((income - 117450) * 0.33 + (117450 - 45500) * 0.25 + (45500 - 11950) * 0.15 + 11950 * 0.1)
    elif income > 190200 and income <= 372950:
        return ((income - 190200) * 0.33 + (190200 - 117450) * 0.33 + (117450 - 45500) * 0.25 + (45500 - 11950) * 0.15 + 11950 * 0.1)
    elif income > 372950:
        return ((income - 372950) * 0.35 + (372950 - 190200) * 0.33 + (190200 - 117450) * 0.33 + (117450 - 45500) * 0.25 + (45500 - 11950) * 0.15 + 11950 * 0.1)

def main():

    # Read filing status
    status = eval(input("Enter filing status \n1 for single \n2 for Married filing jointly\
		\n3 for Married filing separately\n4 for Head of household:\n"))

    # Error checking
    while status < 1 or status > 4:
        status = eval(input("Invalid filing status. Please enter valid filing status: "))
    print()

    # Gather user input for income
    taxable_income = eval(input("Input taxable income: "))
    if (status == 1):
        final = tax_1(taxable_income)
    elif (status == 2):
        final = tax_2(taxable_income)
    elif (status == 3):
        final = tax_3(taxable_income)
    elif (status == 4):
        final = tax_4(taxable_income)

    # Final message
    message = ("The tax for the individual is ${:,.2f}" .format(final))
    tkinter.messagebox.showinfo("Final Info", message)


main()
