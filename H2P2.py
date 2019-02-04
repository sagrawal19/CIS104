#  user entering  title of the book, name of the author, publish year of the book.total number of pages 
Book_title = input("Please Enter The Title of The Book :")
author_name = input("Please Enter The Name of The Author :")
book_Year = int(input("Please Enter The Publish Year of The Book :"))
book_Page = int(input("Please Enter The Total Number of Page in the Book :"))

# Now write an expression to calculate how old the book is. Assign this result to a new variable.
#  3. Write a conditional if-else statement that conforms to the following rules:
# If the age of the book is less than 10 years old, output: “This book is younger than ten years old.”
# Otherwise, output: “This book is at least ten years old.”
book_age = 2019 - book_Year

if (book_age <= 10):
    print("This book is younger than ten years old.")
else:
    print("This book is at least ten years old. ")

# • If the number of pages in the book is less than 100, output: “This book is a short book.”
# If the number of pages in the book is between 100 and 300, output: “This book is an average book.”
# Otherwise, output: “This book is a long book.”

if (book_Page <= 100):
    print("This book is a short book.")
elif (book_Page > 100 & book_Page < 300):
    print("This book is an average book.")
else:
    print("This book is a long book.")
