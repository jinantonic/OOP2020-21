# course: Object-oriented programming, year 2
# academic year: 2020-21
# author: Jina Park
# date: 18-05-2021
# purpose: OOP Semester 2 Exam

# A function that accepts a string argument and returns a value indicating
# if the string matches a particular regular expression.

# Function body evaluates the argument and determines if it is a date
# in the format DD[.|-]MM[.|-]YYYY, where the year should accept only values starting at 2000
import datetime

def find_function(str):
    date = []
    
    if(str[0].isalpha()):
        result = str.find('Jina')
        if(result != -1):
            print("Word found in the given string")
        else:
            print("Boo")

    else: 
        try:
            date = str.split('.')
        except ValueError:
            date = str.split('-')
        
        print(date)
        isValid = True
        year = int(date[2])
        month = int(date[1])
        day = int(date[0])

        try:
            datetime.datetime(year, month, day)
        
        except ValueError:
            isValid = False
            #raise ValueError("Incorrect data format")

        if(isValid and year >= 2000):
            print("Valid input date" )
        elif(year < 2000):
            print("Year should be greater than 2000")
        else:
            print("Invalid input date")
        

find_function("Park from South Korea")
find_function("19.1.1995")
find_function("19.15.2022")

