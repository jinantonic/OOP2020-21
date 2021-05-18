# course: Object-oriented programming, year 2
# academic year: 2020-21
# author: Jina Park
# date: 18-05-2021
# purpose: OOP Semester 2 Exam

# A function that accepts a string argument and returns a value indicating
# if the string matches a particular regular expression.
def find_function():
    str = "Jina Park from South Korea"
    result = str.find('Jina')
    if(result != -1):
        print("Word found in the given string")

find_function()


# Function body evaluates the argument and determines if it is a date
# in the format DD[.|-]MM[.|-]YYYY, where the year should accept only values starting at 2000
import datetime

def validate(day, month, year):

    isValid = True

    try:
        datetime.datetime(int(year), int(month), int(day))
    
    except ValueError:
        isValid = False
        #ßraise ValueError("Incorrect data format")

    if(isValid):
        print("Valid input date" )
    elif(year < 2000):
        print("Year should be greater than 2000")
    else:
        print("Invalid input date")
        

validate(19, 1, 1995)
validate(19, 15, 2022)

