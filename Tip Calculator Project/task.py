print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give?10, 12 or 15?"))/100
split = int(input("How many people to split the bill? "))
each_pay = round(((bill + bill*percentage)/split),2)
print(f"Each person should pay: {each_pay}")