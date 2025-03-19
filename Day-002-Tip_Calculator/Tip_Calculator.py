print("Welcome to the tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill?"))

split_amount = bill*(1+(tip/100))/split

print(f"Each person should pay: ${round(split_amount,2)}")
