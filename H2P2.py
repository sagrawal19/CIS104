#  user entering  title of the book, name of the author, publish year of the book.total number of pages 
Book_title = input("Please Enter The Title of The Book :")
author_name = input("Please Enter The Name of The Author :")
book_Year = int(input("Please Enter The Publish Year of The Book :"))
book_Page = int(input("Please Enter The Total Number of Page in the Book :"))
# calculate the year
import datetime
now = datetime.datetime.now()
# print(now.year)
book_age = now.year - book_Year
# conditional statement for book age
if (book_age <= 10):
    print("This book is younger than ten years old.")
else:
    print("This book is at least ten years old. ")

# conditional statement for book page
if (book_Page <= 100):
    print("This book is a short book.")
elif (book_Page > 100 & book_Page < 300):
    print("This book is an average book.")
else:
    print("This book is a long book.")
