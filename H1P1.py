first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")
age = input("please enter your age:")
confidence =int( input("Please enter your confidence in programmer between 0-100%:"))
dog_age = int(age)*7
print("Hello ",first_name ," ",last_name, ",nice to meet you!\nYou might be ",age," in human years,but in dog years you are ",dog_age)
if(confidence/100) < .5:
    print("I agree,programmers can't be trusted!")
else:
    print("Writing good code takes hard work!")