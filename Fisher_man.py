# Ask the user for the weight of the fish in pounds
weight_pounds = float(input("How many pounds of fish did you catch? "))

# Convert the weight to kilograms
weight_kilos = weight_pounds / 2.20462

# Calculate the price of the fish
price = weight_kilos * 2

# Check if the price is greater than 1
if price > 1:
    print("Congratulations! You caught", weight_pounds, "pounds of fish and earned a hook as a prize!")
else:
    print("You caught", weight_pounds, "pounds of fish and were fined for not catching enough.")

# Print the final price
print("The price of your fish is $", round(price, 2))