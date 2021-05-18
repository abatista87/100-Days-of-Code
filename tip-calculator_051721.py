#Begin Tip Calculator
print ("Welcome to the tip calculator.")
tbill = input("What was the total bill? $")
#Make tbill an int
tbill = float(tbill)
#tbill = tbill * 100
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage = int(percentage) /100
split = input("How many people to split the bill? ")
split = int(split)
split_bill = (tbill + tbill * percentage) / split

print (f"Each person should pay: ${split_bill:.2f}")
