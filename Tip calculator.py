"""
    Calculate tip amount based on meal price and custom tip percentage.

meal_price: price of the meal from user input
custom_tip: desired tip percentage from user input
"""

def calculate_tips():
    # Get user input for meal price and custom tip percentage
    meal_price = float(input("Enter the meal price: "))
    custom_tip = float(input("Enter your custom tip percentage: "))
    while meal_price < 0 or custom_tip < 0:
        print("Invalid input. Please enter non-negative values.")
        meal_price = float(input("Enter the meal price: "))
        custom_tip = float(input("Enter your custom tip percentage: "))
    # Calculate tip amounts
    mint = meal_price * 15 /100
    midt = meal_price * 20 /100
    majt = meal_price * custom_tip/100 # Custom tip calculation

    # Round tip amounts to 2 decimal places
    minor_tip = round(mint, 2)
    middle_tip = round (midt, 2)
    major_tip = round (majt, 2)

    # Format tip amounts as strings with 2 decimal places
    tips = [minor_tip, middle_tip, major_tip]
    formatted_tips = [f"{tip:.2f}" for tip in tips]

    # Provide feedback based on custom tip amount (using numeric values)
    if major_tip < minor_tip and major_tip < middle_tip:
        return f"tip-> {formatted_tips[2]} You're an economist. great!"
    elif major_tip > minor_tip and major_tip > middle_tip:
        return f"tip-> {formatted_tips[2]} So generous. Thank you!"
    elif major_tip == minor_tip or major_tip == middle_tip:
        return f"tip-> {formatted_tips[2]} You know the business!"

    return f"Your tips calculated: 15% = {formatted_tips[0]}, 20% = {formatted_tips[1]}, custom {custom_tip}% = {formatted_tips[2]}"


print(calculate_tips())