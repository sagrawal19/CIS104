
Pennies = input("How many pennies do you have:")

Nickels = input("How many Nickels do you have:")
Dimes = input("How many Dimes do you have:")
Quarters = input("How many Quarters do you have:")
Half_dollars = input("How many Half dollars do you have:") 
Dollars = input("How many Dollars do you have:")

if int(Pennies) <=1:
    print("You have ",Pennies," penny")
else:
    print("You have ",Pennies, " pennies")
if int(Nickels) <=1:
    print("You have ",Nickels, " nickel")
else:
    print("You have ",Nickels, " nickels")
if int(Dimes) <=1:
    print("You have ",Dimes, " dime")
else:
    print("You have ",Dimes, " dimes")
if int(Quarters) <=1:
    print("You have ",Quarters, " quarter")
else:
    print("You have ",Quarters, " quarters")
if int(Half_dollars) <=1:
    print("You have ",Half_dollars, " half dollar")
else:
    print("You have ",Half_dollars, " half dollars")
if int(Dollars) <=1:
    print("You have ",Dollars, " dollar")
else:
    print("You have ",Dollars, " dollars")
Total_value = (int(Dollars)*100) + (int(Half_dollars)*50) + (int(Quarters)*25) + (int(Dimes)*10) + (int(Nickels)*5) + int(Pennies)
print("The value of all of your coins is:$",Total_value/100)