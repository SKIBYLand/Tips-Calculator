"""
    Calculate tip amount based on meal price and custom tip percentage.

meal_price: price of the meal from user input
custom_tip: desired tip percentage from user input
"""

def calculate_tips():
    # Get user input for meal price and custom tip percentage
    meal_price = float(input("Enter the meal price: "))
    custom_tip = float(input("Enter your custom tip percentage: "))
    # Calculate tip amounts
    mint = meal_price * 15 /100
    midt = meal_price * 20 /100
    majt = meal_price * custom_tip/100 # Custom tip calculation

    # Round tip amounts to 2 decimal places
    minor_tip = round (mint, 2)
    middle_tip = round (midt, 2)
    major_tip = round (majt, 2)

    # Format tip amounts as strings with 2 decimal places
    tips = [minor_tip, middle_tip, major_tip]
    # Create a list of formatted tip amounts. Assign to meal_price variable.
    meal_price = [f"{tip:.2f}" for tip in tips]

    return meal_price

print(calculate_tips())