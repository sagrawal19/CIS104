import calculator
import math
# choice for operator
operator = ''
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("r.Recall")
print("i.Invert")
print("c.Clear")
print("x.Exit")

# while loop for calculation
while(True):
    
    choice = input("Enter choice(1/2/3/4/5/r/i/c/x):")

    if choice == 'r':
       print(calculator.getMemoryValue())
       continue
    elif choice == 'i':  
        print(calculator.invert())
        continue
    elif choice == 'c':   
        print(calculator.clearMemory())  
        continue
    elif choice == 'x':
        break
    
    if choice != '1' and choice != '2' and choice != '3' and choice != '4'and choice != '5'and choice != 'r' and choice != 'i'and choice != 'c':  
        print("Invalid choice")
        continue
    if operator == '':
        leftValue = int(input("Enter first number: "))
    else:
        leftValue = calculator.getMemoryValue()  
    operator = choice  
    
    rightValue = int(input("Enter second number: "))

    if choice == '1':
        currentValue = calculator.add(leftValue,rightValue)
        print(leftValue,"+",rightValue,"=",currentValue)
        calculator.setMemoryValue(currentValue)
        print (calculator.getMemoryValue())

    elif choice == '2':
        currentValue = calculator.subtract(leftValue,rightValue)
        print(leftValue,"-",rightValue,"=",currentValue)
        calculator.setMemoryValue(currentValue)

    elif choice == '3':
        currentValue = calculator.multiply(leftValue,rightValue)
        print(leftValue,"*",rightValue,"=",currentValue)
        calculator.setMemoryValue(currentValue)

    elif choice == '4':
        currentValue = calculator.divide(leftValue,rightValue)
        print(leftValue,"/",rightValue,"=",currentValue)
        calculator.setMemoryValue(currentValue)
    elif choice == '5':
        currentValue = calculator.power(leftValue,rightValue)
        print(leftValue,"^",rightValue,"=",currentValue)
        calculator.setMemoryValue(currentValue)    
    else:
        print("Invalid input")