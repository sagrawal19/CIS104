def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
        
print("output:::",monkey_trouble(True,True))
#true
print("output:::",monkey_trouble(False, False)) 
# True
print("output:::",monkey_trouble(True, False))
# False
