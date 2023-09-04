print("\n")
while True:
    try:
        price_of_food = float(input("What is the price of your food?  "))
        break
    except ValueError:
        print()
        print("Your input was invalid. Please enter your price in digits not in words.")
        print()

#Calculate tip percent
tip_percent = 18 / 100 * price_of_food
rounded_value1 = round(tip_percent, 2)

#calculate sales tax
sales_tax = 7 / 100 * price_of_food
rounded_value2 = round(sales_tax, 2)

#The total amount comprises the food cost + tax and tips.
total_amount = price_of_food + tip_percent + sales_tax
rounded_value3 = round(total_amount, 2)

#All charges payable by customer
print("\n")
print(">>> Tips (18%) = $" + str(rounded_value1))
print("\n")
print(">>> Sales Tax (7%) = $" + str(rounded_value2))
print("\n")
print(">>> Total charge = $" + str(rounded_value3))
print("\n")
