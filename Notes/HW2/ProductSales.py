# Program to compute product sales

import tkinter.messagebox
def main():
    # Set the prices
    product_1_price = 2.98
    product_2_price = 4.50
    product_3_price = 9.98
    product_4_price = 4.49
    product_5_price = 6.87

    # Gather user input
    product_id, amount = eval(input("Enter the product number followed by the quantity sold: "))
    total_products_sold = 0
    total_amount = 0
    while product_id != -1:
        if product_id >= 1 and product_id <= 5:
            if product_id == 1:
                total_amount += amount * product_1_price
            elif product_id == 2:
                total_amount += amount * product_2_price
            elif product_id == 3:
                total_amount += amount * product_3_price
            elif product_id == 4:
                total_amount += amount * product_4_price
            elif product_id == 5:
                total_amount += amount * product_5_price
            total_products_sold += amount
        else:
            print ("You put an incorrect product number. Try again")
        product_id, amount = eval(input("Enter the product number followed by the quantity sold. Enter -1,1 to signal that you're done: "))
    if total_products_sold == 0:
        print ("No items sold.")
    elif total_products_sold >= 1:
        print ("Total value of %d products sold is $%.2f" % (total_products_sold,total_amount))
        tkinter.messagebox.showinfo("Final Information", "Total value of %d products sold is $%.2f" % (total_products_sold,total_amount))

main()
