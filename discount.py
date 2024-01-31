from datetime import datetime

print("Welcome to the Discount Calculator!")

# Get the current day of the week
today = datetime.now().weekday()

# Get the subtotal from the user
subtotal = float(input("Enter the subtotal: $"))

# Calculate discount
if subtotal >= 50 and (today == 1 or today == 2):  # Tuesday or Wednesday
    discount = subtotal * 0.10
    print(f"Discount applied: ${discount:.2f}")
else:
    discount = 0

# Calculate sales tax
sales_tax = subtotal * 0.06

# Calculate total amount due
total_amount_due = subtotal - discount + sales_tax

print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total amount due: ${total_amount_due:.2f}")