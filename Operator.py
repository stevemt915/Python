#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal,
# find and print the meal's total cost. Round the result to the nearest integer.

def solve(meal_cost, tip_percent, tax_percent):
    # Calculate tip and tax amounts
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    
    # Calculate total cost
    total_cost = meal_cost + tip + tax
    
    # Round the total cost to the nearest integer
    total_cost_rounded = round(total_cost)
    
    return total_cost_rounded

# Read inputs
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

# Calculate total cost
total_cost = solve(meal_cost, tip_percent, tax_percent)

# Print the result
print(total_cost)