print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
shares = int(input("How many people to split the bill? "))

print("Each person should pay: $", round((bill + bill * tip / 100) / shares, 2))