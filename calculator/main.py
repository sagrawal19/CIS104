import calculator
import math


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("x.Exit")

while(True):
    
    choice = input("Enter choice(1/2/3/4/x):")
    if choice == 'x':
        break
    if choice != '1' and choice != '2' and choice != '3' and choice != '4':  
        print("Invalid choice")
        continue
    leftValue = int(input("Enter first number: "))
    rightValue = int(input("Enter second number: "))

    if choice == '1':
        print(leftValue,"+",rightValue,"=",calculator.add(leftValue,rightValue))

    elif choice == '2':
        print(leftValue,"-",rightValue,"=",calculator.subtract(leftValue,rightValue))

    elif choice == '3':
        print(leftValue,"*",rightValue,"=",calculator.multiply(leftValue,rightValue))

    elif choice == '4':
        print(leftValue,"/",rightValue,"=",calculator.divide(leftValue,rightValue))
    else:
        print("Invalid input")