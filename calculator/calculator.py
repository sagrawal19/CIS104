import math

currentValue = 0
memoryValue =  0



# Function to add two numbers
def add(leftValue, rightValue): 
        result =leftValue + rightValue
        return result
        
    
# Function to subtract two numbers  
def subtract(leftValue, rightValue):  
        result= leftValue- rightValue
        return result
        

# Function to multiply two numbers 
def multiply(leftValue, rightValue):  
        result =leftValue* rightValue 
        return result
       

# Function to divide two numbers 
def divide(leftValue, rightValue):  
        result =leftValue /rightValue
        return result
      


# i.	Memory Store: Store the calculator’s current value in the memory value.
def setMemoryValue(value):
    global memoryValue
    global currentValue
    memoryValue = value
    currentValue = value

#j.	Memory Recall: Change the calculator’s current value to whatever is in the memory value, and returns the new current value.
def getMemoryValue():
    return memoryValue

#k.	Current Clear: Clear the memory value.
def clearCurrent():
    global currentValue
    currentValue = 0

#k.	Memory Clear: Clear the memory value.
def clearMemory():
    global memoryValue
    memoryValue = 0
    return memoryValue

#l.	Invert: Invert the sign of the calculator’s current value, and returns the new current value.
def invert():
        global currentValue
        result = -1*currentValue
        return result
        

#m.	Power: Calculates the calculator’s current value to a specific power, and returns the new current value.
def power(leftValue, rightValue):  
        result =leftValue ** rightValue
        return result
        #print(result)
