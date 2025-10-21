"""
    Calculate tip amount based on meal price and custom tip percentage.

meal_price: float(input("Enter the meal price: ))
custom_tip: float(input("Enter your custom tip percentage: ))
"""

def calculate_tips():
    meal_price = float(input("Enter the meal price: "))
    custom_tip = float(input("Enter your custom tip percentage: "))
    mint = meal_price * 15 /100
    midt = meal_price * 20 /100
    majt = meal_price * custom_tip/100

    minor_tip = round (mint, 2)
    middle_tip = round (midt, 2)
    major_tip = round (majt, 2)

    tips = [minor_tip, middle_tip, major_tip]
    meal_price = [f"{tip:.2f}" for tip in tips]

    return meal_price

print(calculate_tips())