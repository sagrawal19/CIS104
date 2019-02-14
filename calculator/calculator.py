import math

#leftValue = 0
#print(leftValue)
#rightValue = 0
#print (rightValue)
#result = 0  
#print(result)

#def clear():
currentValue = 0
memoryValue =0

def setMemoryValue(value):
    memoryValue = value

def getMemoryValue():
     return memoryValue 

# Function to add two numbers
def add(leftValue, rightValue): 
        result =leftValue + rightValue
        return result
        #print(result)
    
# Function to subtract two numbers  
def subtract(leftValue, rightValue):  
        result= leftValue- rightValue
        return result
        #print(result)
  
# Function to multiply two numbers 
def multiply(leftValue, rightValue):  
        result =leftValue* rightValue 
        return result
        #print(result)
# Function to divide two numbers 
def divide(leftValue, rightValue):  
        result =leftValue /rightValue
        return result
        #print(result)
# i.	Memory Store: Store the calculator’s current value in the memory value.


#j.	Memory Recall: Change the calculator’s current value to whatever is in the memory value, and returns the new current value.
#k.	Memory Clear: Clear the memory value.
#l.	Invert: Invert the sign of the calculator’s current value, and returns the new current value.
#m.	Power: Calculates the calculator’s current value to a specific power, and returns the new current value.
