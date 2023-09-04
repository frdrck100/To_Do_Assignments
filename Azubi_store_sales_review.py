#Week 3 python To_Do assignment

# Define the data
print()
products = [
    "Sankofa Foods", 
    "Jamestown Coffee", 
    "Bioko Chocolate", 
    "Blue Skies Ice Cream", 
    "Fair Afric Chocolate", 
    "Kawa Moka Coffee", 
    "Aphro Spirit", 
    "Mensado Bissap", 
    "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Average price for all produts
total_price_average = sum(prices) / len(prices)
print()
rounded_value1 = round(total_price_average, 2)
print("Total Price Average: ", rounded_value1)

# New price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]
print()
print("New Prices:", new_prices)

# Total revenue generated from the products
total_revenue = sum([price * customers for price, customers in zip(prices, last_week)])
print()
print("Total Revenue:", total_revenue)

# Total revenue generated from the products using the new prices
total_revenue_new_prices = sum([new_price * sold for new_price,sold in zip(new_prices,last_week)])

# calculate the average daily revenue generated from the products using the new prices
avg_daily_revenue_new_prices = total_revenue_new_prices / 7
print()
rounded_value2 = round(avg_daily_revenue_new_prices, 2)
print("The average daily revenue generated is: $", rounded_value2)

# Find products with prices less than $30 based on the new prices
affordable_products = [product for product, price in zip(products, new_prices) if price < 30]
print()
print("Affordable Products:", affordable_products)
print("\n")
