# Write a program that asks the user to input the price and quantity for three different items. Calculate the subtotal, add an 8.5% tax, and display an itemized receipt showing each item’s total and the final amount.

item_1_price = float(input("Enter price of item 1: "))
item_1_quantity = int(input("Enter quantity of item 1: "))
item_2_price = float(input("Enter price of item 2: "))
item_2_quantity = int(input("Enter quantity of item 2: "))
item_3_price = float(input("Enter price of item 3: "))
item_3_quantity = int(input("Enter quantity of item 3: "))

subtotal = (item_1_price * item_1_quantity) + (item_2_price * item_2_quantity) + (item_3_price * item_3_quantity)
total = subtotal * 1.085

print(f"Item 1: {item_1_price} * {item_1_quantity} = {item_1_price * item_1_quantity}")
print(f"Item 2: {item_2_price} * {item_2_quantity} = {item_2_price * item_2_quantity}")
print(f"Item 3: {item_3_price} * {item_3_quantity} = {item_3_price * item_3_quantity}")
print(f"Subtotal: {subtotal}")
print(f"Tax(8.5%): {subtotal * 0.085}")
print(f"Total: {total}")