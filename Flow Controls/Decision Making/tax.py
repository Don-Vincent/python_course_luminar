"""
Ask the price of the bike from the user
if the price is above 2 lakhs add 15% tax and return the total amount(price + tax).
if the price is above 1 lakh and less than or equal to 2 lakhs add 10% tax
if the price is above or equal to 50k and less than or equal to 1 lakh add 7% tax
if price below 50k add tax 5%
"""
price = int(input("Enter the price of the bike: "))

if price > 200000:
    tax = price * 0.15
elif price > 100000:
    tax = price * 0.1
elif price >= 50000:
    tax = price * 0.07
else:
    tax = price * 0.05
print(f"The price of the bike with tax is: {price + tax}")
