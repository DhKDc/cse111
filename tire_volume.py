import math
from datetime import datetime

# Get tire specifications from the user
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))


# Calculate tire volume using the provided formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000.0

# Display the result
print(f"The approximate volume is {volume:.2f} liters.")

# Ask the user if they want to buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

if buy_tires == "yes":
    # Ask for the user's phone number
    phone_number = input("Enter your phone number: ")
    
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open and append to the volumes.txt file
    with open("volumes.txt", "a") as file:
        # Append tire information and phone number to the file
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}\n")

    print("Tire information and phone number have been appended to volumes.txt.")
else:
    print("Thank you for using the Tire Volume Calculator.")