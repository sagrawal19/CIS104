#Given an int n, return True if it is within 10 of 100 . 
# Note: abs(num) computes the absolute value of a number.

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

def near_hundred(n):
    if (n>= 90) and (n <= 110):
        return True
    else:
        return False

print("Checking is the number near to 100 : ", near_hundred(93))
print("Checking is the number near to 100 : ", near_hundred(90))
print("Checking is the number near to 100 : ", near_hundred(89))