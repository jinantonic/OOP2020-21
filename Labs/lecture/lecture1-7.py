# string concatenation
sirname = 'Jina'
conjunction = 'and'
lastname = 'Park'
print(sirname + conjunction + lastname)

## Formatters
# formatting strings with %
name = 'Jina'
age = 25
print("%s is %d years old" % (name, age))
# We can include spaces in the representation with giving a number of spaces
print("%10d" % (12))
# %f formats decimal numbers, example uses 4.2f (4 = total length, 2 = decimal positions)
print("%4.2f" % (1.123))
print("%7.2f" % (1.123)) # 7 spaces in total, 3 leading space characters, 2 decimal points
# format() method -> "strings to be formatted".format(values tor variables to be inserted into string, separated by comma)
brand = 'Samsung'
exchange_rate = 5.2
message = "The price of this {0:s} smartphone is {1:d} EUR and the exchange rate to British Pound is {2:4.2f} to 1 EUR" . format(brand, 555, exchange_rate)
print(message)
# count(sub, [start, [end]]) returns the no of times the substring sub appears in a string, case sensitive function
print('This is a string' .count('s'))  # s occurs at index 3, 6 and 10
print('This is a string' .count('s', 4))  # counts from index 4
print('This is a string' .count('s', 4, 10))  # counts from index 4 to 9(10-1)
print('This is a string' .count('t')) # the function is case sensitive
# endswith(suffix, [start, [end]]) returns if the string ends with a specified suffix, otherwise returns false, suffix can also be a tuple of suffixes, case sensitive function
print('Postman' .endswith('man'))  # man occurs in the index 4-6
print('Postman' .endswith('man', 3))  # checks from index 3 to end
print('Postman' .endswith('man', 2, 6))  # checks from index 2 to 5
print('Postman' .endswith('man', 2, 7))  # true
# find/index (sub, [start, [end]]) returns the index in a string, where the first occurence of the substing is found
# find() returns -1 if sub is not found and index() returns ValueError if sub is not found
print('This is a string' .find('s'))
print('This is a string' .find('s', 4))
print('This is a string' .find('s', 7, 11))
#print('This is a string' .find('o'))
#print('This is a string' .index('o'))
# isalnum() returns true if all characters in a string are alphanumeric and there is at least one character (false or otherwise)
# Does not include whitespaces and alphanumeric is either a letter or a number
print('abc123' .isalnum())
print('a b c 1 2 3' .isalnum())
print('abc' .isalnum())
print('123' .isalnum())
# isalpha() returns true if all characters in the string are alphabetic and there is at least one character (true or otherwise)
print('abc' .isalpha())
print('abc123' .isalpha())
print('123' .isalpha())
print('a b c' .isalpha())
# isdigit() returns true if all characters in the string are digits, and there is at least one character (true or otherwise)
print('123' .isdigit())
print('123abc' .isdigit())
print('abc' .isdigit())
print('1 2 3' .isdigit())
# print('二' .isdit()) isnumeric is true if we feed it a digit from any language Python recognises
print('二' .isnumeric())
# similar functions islower(), isspace(), istitle(), isupper()
# join() returns a string where the parameter provided is joined by a separator
separator = '-'
my_tuple = ('a', 'b', 'c')
my_list = ['d', 'e', 'f']
my_string = "Hello World"
print(separator .join(my_tuple))
print(separator .join(my_list))
print(separator .join(my_string))
# replace(old, new[, count]) returns a copy of a string with all occurrences of substring old replaced by substring new, case senstive function
# count is options, means that only these amount of instances are replaced
print('This is a string' .replace('s', 'p'))
print('This is a string' .replace('s', 'p', 2))
# split[sep, [maxsplit]]) returns a list of words in a string
# If sep is not given, use whitespace. If maxsplit is given, this is the maximum no of splits performed, case sensitive function
print('This, is, a, string' .split(','))
print('This is a string' .split(','))
print('This, is, a, string' .split(',', 2))
# splitlines([keepends]) returns a list of lines, break at boundary. Linebreaks are not included unless keepends is used and true
print("This is the first line. \This is the second line." .splitlines())
print("This is the first line."
      "This is the second line." .splitlines())
print("This is the first line. \This is the second line." .splitlines(True))
# new line : \n, tab : \t
# strip([chars]) returns a copy of a string with the leading and trailing characters char removed. If char is not provided, the function uses whitespaces
print("      This is a string" .strip())
print("This is a string" .strip('s'))
print("This is a string" .strip('g'))
# slices
user_age = [10, 20, 30, 40, 50, 60 ,70]
print(user_age[1:3])
print(user_age[:4]) # returns values from 0 to 3(4-1)
print(user_age[1:]) # returns values from index 1 to length-1
print(user_age[:])
print(user_age[1:6:2])
print(user_age[-1]) # the last index
print(user_age[-2]) # the second last index

user_age[3] = 99
print(user_age)
user_age.append(100)
print(user_age)
del user_age[3]
print(user_age)

# lists
my_list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del my_list2[2]
print(my_list2)
del my_list2[1:5]
print(my_list2)
del my_list2[:3]
print(my_list2)
del my_list2[2:]
print(my_list2)
# extend() combines two lists
my_list3 = ['a', 'b', 'c']
my_list4 = [1, 2, 3]
my_list3.extend(my_list4)
print(my_list3)
# in() true if the parameter is in the list, false otherwise
print('c' in(my_list))
# insert() adds an item at a particular position
my_list3. insert(1, 'Hi')
print(my_list3)
# len() calculates the no of items
print(len(my_list3))
# pop() gets an item at index position and remove it from the list
my_list5 = ['a', 'b', 'c']
member = my_list5.pop(2) # removes the last item on the list if no argument is given
print(member)
print(my_list5)
# remove() removes an item from a list and requires a specific value
my_list5.remove('a')
print(my_list5)

my_list8 = [5,10,2,90,1]
my_list8.reverse()
print(my_list8)

#my_list8 = sorted(my_list1) # causes an error
my_list8.sort() #changes the list in place, no copy returned
print(my_list8)

print(sorted(my_list8)) #creates a copy and returns it
print(my_list8) #original unchanged
print(my_list8*2)

print(int('3')+3) #casting

# tuples
# del deletes a complete tuple
months = ('Jan', 'Feb', 'Mar')
days = ('Mon', 'Tue', 'Wed')
# del months
print(months)
# Jan in my tuple -> true
print('Jan' in(months))
# len calculates the length of the tuple
print(len(days))
# + concatenates tuples
print(months + days)
# * multiple tuples
print(days * 7)

# sets
hello = set('hello')
print(hello)

# dictionary
customers = {"Jina":25, "Ovid":8, "Skittles":1}
print(customers)
customers["Ovid"] = 7 # modify
print(customers)
del customers["Ovid"] # remove
print(customers)
#customers.clear() # empty
#print(customers)
print(customers.get("Jina")) # get() returns a value for a given key
print('Jan' in(customers)) # in checks if an item is in the dictionary
print(customers.items()) # items() returns a list of dictionary pairs as tuples
print(customers.keys()) # keys() returns a list of dictionary keys
print(customers.values()) # values() returns a list of dictionary values
print(len(customers)) # len() returns a number of items in dictionary
dict1 = {1 : 'one', 2 : 'two'}
dict2 = {1 : 'one', 3 : 'three'}
dict1.update(dict2)
print(dict1)
# type casting
num1 = 13.456
num2 = 154
print(int(num1)) # int() takes a float or appropriate string and converts it into an integer
print(float(num2)) # float() takes an integer or an appropriate string and converts it into a float
print(str(num1)) # str() converts an integer or a float into a string
print(str(num2))

print(type(-5e10))

first_name = 'Jina'
last_name = 'Park'
msg = f'Hello, {first_name} {last_name}'
# f' means literal string where we see expressions inside brackets. Ther expressions are being replaced.
print(msg)

# for loops
pets = ["Horse", "Dog", "Cat", "Hamster"]
for mypets in pets:
      print(mypets)
# eg without enumerate() means that you have to keep track manually of your iterating counter variable, here called i
i = 0
for mypets in pets:
      print("index is %d and value is %s" % (i, mypets))
# iterate with index enumerate
for index, mypets in enumerate(pets):
      print(index, mypets)
# loop through a string
msg_2 = "Hello World"
for i in msg_2:
      print(i)
# range(start, step, end)
# start : optional int, default is 0 / end : mandatory int, defines where to stop / step : optional int, default is 1
for i in range(4):
      print(i)

for i in range(10):
      print(i, end =" ")

counter = 4
while counter > 0:
      print("Counter: ", counter)
      counter -= 1

j = 0
for b in range(12):
      j += 3
      print("j: ", j, "and b: ", b)
      if j == 6:
            break

try: # try do something
      result = 4 / 0
      print(result)
except ZeroDivisionError: # do something else in case of an error
      print("Can't divide by zero")
except Exception as e:
      print("Unknown error")

name = ["Bianca", "Bryan", "Susan"]
city = ("Dublin", "Galway", "Cork")
print(name)
print(id(name))
print(city)
print(id(city))

print(name[0])
print(city[0])

name[0] = "Lucas"
print(name[0])
#city[0] = "Portlaoise"
#print(city[0])

print("name location: ", id(name))
print("city location: ", id(city))
name += ["Bianca", "Paul"] # 리스트의 끝에 두개의 이름 추가
city += ("Portlaoise", "Swords")
print(name)
print(city)
print("After change name location: ", id(name)) # Same
# address in memory
print("After change city location: ", id(city)) # New address in memory
# Other immutable data types
age = 21
print(id(age))
age += 1
print(age)
print(id(age))

name_ = "Jina"
print(id(name_))
name_ += "Park"
print(id(name_))

# Copying mutable objects by reference
name2 = name # creates a copy  by reference
print(id(name))
print(id(name2))
name.append("Jina")
print(name is name2) # is checks for the memory address
print(name)
print(name2)

# copying lists not by reference
name3 = name[:] # not a copy by reference
name4 = list(name) # not a copy by reference
print(id(name))
print(id(name2))
print(id(name3))
print(id(name4))

name.append("Park")
print(name is name2)
print(name is name3)
print(name is name4)
print(name)
print(name2)
print(name3)
print(name4)

try:
      print(name[8])
# as denotes that the name after is an alias별명 for what's before. This is often used for shorhand of long names. Exceptions names can get very long.
except IndexError as ie:
      print("This index position does not exist."
            "Caused error :\n", ie)
except Exception as e:
      print("Unexpected error occurred : \n", e)

print("Still here. We haven't crashed")

class EvenOnly(list):
      def append(self, integer):
            if not isinstance(integer, int):
                  raise TypeError("Only integers can be added")
            if integer % 2:
                  raise ValueError("Only even numbers can be added")
            super().append(integer)

even = EvenOnly()
# even.append("hello World") only integers can be added
# even.append(13) only even numbers can be added

def my_division(myNumber):
      try:
            return 100 / myNumber
      except (ZeroDivisionError, TypeError):
            return "Enter a number that is not zero"

for value in ('0', 50.0, 'hello', 13):
      print('Testing {}: '.format(value), end=" ")
      print(my_division(value))

#def my_division2(myNumber):
      #try :
            #if myNumber == 13:
                  #raise ValueError("13 is an unlucky number")
            #return 100 / myNumber
      #except ZeroDivisionError:
            #return "Enter a number other than zero"
      #except TypeError:
            #return "Enter a numerical value"
      #except ValueError:
            #print("No, no, not 13!")
            #raise

#for value in ('0', 50.0, 'hello', 13):
      #print('Testing {}: '.format(value), end=" ")
      #print(my_division2(value))

def testingArguments():
      try:
            raise ValueError("This is a test argument")
      except ValueError as e:
            print("The exception arguments are: ", e.args)

testingArguments()

some_exceptions = [ValueError, TypeError, IndexError, None]
try:
      choice = some_exceptions[3] # change values here from 0 to 3
      print("raising {}.".format(choice))

except ValueError:
      print("Caught a ValueError")
except TypeError:
      print("Caught a TypeError")
except Exception as e:
      print("Caught someother error: %s" % e.__class__.__name__)
else:
      print("This code called if there is no exception")
finally:
      print("This cleanup code is always called")

# my own exception
#class InvalidStudentEnrollment(Exception):
      #pass
#raise InvalidStudentEnrollment("Not a valid student for this programme.")

# You can include any amount of arguments
#class InvalidStudentEnrollment2(Exception):
#     def __init__(self, studentID, name):
#           super().__init__("Invalid student ${}". format(name))
#          self.studentID = studentID
#          self.name = name
#    def auditInvalidStudent(self):
#           return self.name + ' ' + self.studentID

#raise InvalidStudentEnrollment2(119, "Jina Park")

#F = open("myFile.txt", "w")
#print(F)
#F.write('first line \n') # write() by itself does not add a newline character
#F.write("Second line")
#F.close()

#F = open("myFile.txt", "r")
#print(F.read())
#F.close()
#print(F.read(5))
#F.close()
#print(F.readline()) # readline() reads a string and automatically adds newline character apart from the last line
#F.close()
#print(F.readlines())
#F.close()

#F = open("myFile.txt", "r")
#for line in F:
#    print(line)
#F.close()
#F = open("myFile.txt", "r")
#for line in F:
#    word = line.split()
#    print(word)
#F.close()

# for an automatic close use with
#with open("myFile.txt", "a") as file_obj:
#      file_obj.write("hello")

# Dictionary creating and accessing
stocks = {"GOOG" : (613.04, 625.15, 610.08),
          "MSFT" : (30.25, 30.70, 30.19)}
print(stocks["GOOG"])
print(stocks["MSFT"])
print(stocks.setdefault("RIM", (20.00, 24.22, 30.01)))
print(stocks.keys())
print(stocks.values())
print(stocks.items())
for stock, values in stocks.items():
      print("{} last value is {}".format(stock, values[0]))

# key can be everything but lists
randomKey_Dict = {}
randomKey_Dict["hello"] = "world"
randomKey_Dict[22] = 'twenty two'
randomKey_Dict[2.2] = 'two point two'
randomKey_Dict[('abc', 123)] = 'tuples work'
try:
      randomKey_Dict[[1, 2, 3]] = 'no lists'
except:
      print("no lists")

class myDictObject:
      def __init__(self, myValue):
            self.myValue = myValue
myObject = myDictObject(30)
randomKey_Dict[myObject] = 'I like objects'

for key, value in randomKey_Dict.items():
      print("{} has value {}".format(key, value))

# Counter behaves like a dictionary, where the keys are the items to be counted and the values are the numbers
from collections import Counter
def letter_frequency(sentence):
      return Counter(sentence)
print(letter_frequency("hello world"))

# sorting a list
mylist9 = ['Hello', 'Help', 'Hallo', 'Heyo']
mylist9.sort()
mylist9.sort(key=str.lower)
print(mylist9)

# set -  creating a list of (song, artist) tuples + set of artists
songs =[("Big Bang", "Big Bang"),
        ("Lie", "Jina Park"),
        ("Heaven", "Big Bung"),
        ("Last Farewell", "Big Bong")]
artists = set()
for song, artist in songs:
      artists.add(artist)
print(artists)
for artist in artists:
      print(artist)

inOrder = list(artists)
inOrder.sort()
print(inOrder)

myArtists = {"Big Bang", "Jina Park", "Jina Kim", "Big Bong", "Frank Ocean", "Hashbrown"}
friendArtists = {"Jina Kim", "Jina Park"}
print("All artists :{}".format(myArtists.union(friendArtists)))
print("Both artists :{}".format(myArtists.intersection(friendArtists)))
print("Either, but not both :{}".format(myArtists.symmetric_difference(friendArtists)))

print("superset :{}".format(myArtists.issuperset(friendArtists)))
print("superset :{}".format(friendArtists.issuperset(myArtists)))

print("subset :{}".format(myArtists.issubset(friendArtists)))
print("subset :{}".format(friendArtists.issubset(myArtists)))

print("difference :{}".format(myArtists.difference(friendArtists)))
print("difference :{}".format(friendArtists.difference(myArtists)))

# queue FIFO
#from queue import Queue
#line = Queue(maxsize=3)
# block : access to queue is either allowed or denied until an item is available in get, default is True
#line.get(block=False)
#line.put("one")
#line.put("two")
#line.put("three")
#line.put("four", timeout=1)
#if line.full():
      #print("yes, queue is full")
#print(line.get())
#print(line.get())
#print(line.get())
#print(line.empty())

# queue LIFO
#from queue import LifoQueue
#stack = LifoQueue(maxsize=3)
# block : access to queue is either allowed or denied until an item is available in get, default is True
#stack.put("one")
#stack.put("two")
#stack.put("three")
#stack.put("four", block=False)

#print(stack.get())
#print(stack.get())
#print(stack.get())
#print(stack.empty())
#stack.get(timeout=1)

# priority queue
#from queue import PriorityQueue
#heap = PriorityQueue(maxsize=3)
# block : access to queue is either allowed or denied until an item is available in get, default is True
#heap.put((3, "three"))
#heap.put((5, "five"))
#heap.put((2, "two"))
#heap.put((1, "one"), block=False)

#while not heap.empty():
#      print(heap.get())

# tinker first window
#import tkinter as tk
#window = tk.Tk()
#window.mainloop()

# window with a widget
#import tkinter as tk
#window = tk.Tk()
#greeting = tk.Label(text="HELLO WORLD").pack()
#window.mainloop()

# from inside pycharm
# tkinter is the standard binding to Tk. When imported, it loads the Tk library on your system
# ttk is a submodule of tkinter, it implements pythons's binding to the newer themed widgets that were added to Tk in 8.5
#from tkinter import * # we need 2 modules
#from tkinter import ttk # gives us themed widgets, better look and feel then original
#class GUI_Example:
#     def __init__(self):
#            root = Tk() # sets up the main application window
#            ttk.Button(root, text="Hello World").grid() # geometry manager
#            root.mainloop()
#gui_e = GUI_Example()

# the converter program step by step
#class Converter:
#      def __init__(self):
#            self.init_window() # good practice to seperate things out into logical units
#
#     def init_window(self):
#          root = Tk()
#            root.title("Feet to Meters")
#
#            mainframe = ttk.Frame(root, padding="3 3 12 12") # ttk.Frame holds the content of everything
#            mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#            # grid() gets the geometry manager that automatically places everything into the main window
#            root.columnconfigure(0, weight=1)
#            root.rowconfigure(0, weight=1) # columnconfigure/rowconfigure tells tk to expand the window with padding if resized

#      self.feet = StringVar() # self for widgets we want to access throughout the program, first widget is the text box
#      feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
#      feet_entry.grid(column=2, row=1, sticky=(W, E)) # grid() add the widget to the main frame, with position

#      self.meters = StringVar()
#      ttk.Label(mainframe, textvariable=self.meters)\
#            .grid(column=2, row=2, sticky=(W, E))
#      # This is how to call a function from a button
#      ttk.Button(mainframe, text="Calculate", command=self.calculate)\
#            .grid(column=3, row=3, sticky=W)

#      ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W) # sticky determines how things line up
#      ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#      ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

      # sticky option to grid describes how the widget should line up within the grid cell, using compass directions.
      # So W means to anchor the widget to the left side of the cell, WE means to attach it to both the left and right sides
      # python also defines constants for these directional strings, which you can provide as a list eg W or (W,E)

#      for child in mainframe.winfo_children():
#            child.grid_configure(padx=5, pady=5) # adds a bit of padding so items aren't so scrunched

#      feet_entry.focus() # cursor will start here, entry!
#      root.bind("<Return>", self.calculate) # return key defined here to do the same as pressing the button
#      root.mainloop() # crucial to make things appear on screen. It's an event loop

my_array = ["one", "two", "three"]
print(my_array[0])

# nice print
print(my_array)

# Lists are mutable:
my_array[1] = "hello"
print(my_array)

del my_array[1]
print(my_array)

# Lists can hold arbitrary data types:
my_array.append(41)
print(my_array)

# creating lists
squares = []
for i in range(10):
    squares.append(i * i)

print(squares)

# with a comprehension
squares = [i * i for i in range(10)]
print(squares)

# tuple
array = ("one", "two", "three")
print(array[0])
# easy printing
print(array)
# tuples are immutable
# 2 lines below cause an typeerror msg
#array[1] = "hello"
#del array[1]
print(id(array))
array = array + (42,) # adding elements creates a copy of the tuple
print(array)
print(id(array))

# array
import array
array2 = array.array("f", (1.0, 1.5, 2.0, 2.5)) # f is the data type(float)
print(array2[1])
# nice print
print(array2)
# arrays are mutable
array2[1] = 41.0
print(array2)
del array2[1]
print(array2)
array2.append(42.0)
print(array2)
# array2[1] = "hello" will cause error since arrays are typed

# str
array3 = "abcd"
print(array3[1])
# nice print
print(array3)
# strings are immutable
# array3[1] = "e" error
# strings can be unpacked into a list to get a mutable representation
array_list = list("abcd")
print(array_list)

from_1s_to_str = "".join(list("abcd"))
# strings are recursive data structure
print(type(from_1s_to_str))
print(type(from_1s_to_str[0]))

# bytes
array4 = bytes((0, 1, 2, 3))
print(array4)
# bytes literals have their own syntax
print(array4)
array4 = b"\x00\x01\x02\x03"
# only valid bytes are allowed
#print(bytes(0, 300)) out of range error
# bytes are immutable
#array4[1] = 41 error
#del array4[1] error

# bytearray
array5 = bytearray((0, 1, 2, 3))
print(array5[1])
# the bytearray repr
print(array5)
# bytearrays are mutable
array5[1] = 41
print(array5)
print(array5[1])
# bytearrays can grow and shrink in size
del array5[1]
print(array5)
array5.append(42)
print(array5)
# array5[1] = "hello" error because bytearray can only hold bytes
# array5[1] = 255 error -> integers in the range 0 <= x <= 255
# bytearrays can be converted back into byte
# this will copy the data
print(type(array5))
array5 = bytes(array5)
print(type(array5))

# namedtuple
from collections import namedtuple
Car = namedtuple("Car", "color mileage automatic")
my_car = Car("red", 29812.3, False)
# instances have a nice repr
print(my_car)
# accessing fields
print(my_car.mileage)
# fields are immutable
#my_car.mileage = 12
#my_car.windshield = "broken"

from typing import NamedTuple

class Car(NamedTuple):
      color : str
      mileage : float
      automatic : bool

my_car = Car("red", 3812.4, True)
print(my_car)
print(my_car.mileage)
# type annotations are not enforced without a seperate type checking tool like mypy
my_second_car = Car("red", "NOT_A_FLOAT", 99)
print(my_second_car)

# simpleNameSpace
#from types import SimpleNamespace
#my_car = Car(color="red", mileage=3812.4, automatic=True)

# Instances support attribute access and are mutable:
#my_car.mileage = 12
#my_car.windshield = "broken"
#del my_car.automatic
#print(my_car)

# struct
from struct import Struct
my_struct = Struct("i?f")
my_data = my_struct.pack(2, False, 41.0) #packed according to a given format
#                                           #returns a bytes object
# All you get is a blob of data:
print(my_data)
# Data blobs can be unpacked again:
print(my_struct.unpack(my_data))

# class
class Car:
     def __init__(self, color, mileage, automatic):
         self.color = color
         self.mileage = mileage
         self.automatic = automatic
my_first_car = Car("red", 22812.4, True)
my_second_car = Car("grey", 40357.7, False)
# Get the mileage
print(my_second_car.mileage)
# Classes are mutable:
my_second_car.mileage = 12
print(my_second_car.mileage)
my_second_car.windshield = "broken"
print(my_second_car)
# String representation is not very useful
print(my_first_car)

# dataclass
from dataclasses import dataclass
@dataclass
class Car:
      color: str
      mileage: float
      automatic: bool
my_first_car = Car("red", 3812.4, True)
# Instances have a nice repr:
print(my_first_car)
# Accessing fields:
print(my_first_car.mileage)
# Fields are mutable:
my_first_car.mileage = 12
my_first_car.windshield = "broken"
print(my_first_car.mileage)
# Type annotations are not enforced without
# a separate type checking tool like mypy:
my_second_car = Car("red", "NOT_A_FLOAT", 99)
print(my_second_car)

# set
vowels = {"a", "e", "i", "o", "u"}
print("e" in vowels)
letters = set("bianca")
print(letters.intersection(vowels))
vowels.add("x")
print(vowels)
print(len(vowels))

# frozenSet
#vowels = frozenset({"a", "e", "i", "o", "u"})
#vowels.add("p")

# a simple class without behaviour, just a scaffold of a class
class MyDogs:
   pass
# 2 new objects a and b have been instantiated from the class mydogs()
a = MyDogs()
b = MyDogs()
print(a)
print(b)

# # in Python you can add attributes during runtime
a.age = 5
a.colour = "black"
b.age = 2
b.colour = "white"
print(a.age)
print(b.colour)

# class with more methods with more arguments
#class MyDogs:
#  def bark(self):
#      print("wouff wouff")

#  def new_puppy(self):
#      self.age = 0
#      self.eyes = "closed"

#  def run(self, x, y):
#      self.x = x
#      self.y = y

#  def come_when_called(self):
#      self.run(0,0)

#duke = MyDogs()
#rex = MyDogs()
#rex.run(10, 6)
#duke.come_when_called()
#print(rex.x, rex.y)
#print(duke.x, duke.y) # notice that these are not initialised anywhere at the start
# # dog without x and y:
#luna = MyDogs()
#print(luna.x) #gives an error message that MyDogs doens't have an x attribute

print("Can passenger {} please go to flight {}".format("Bianca", 123))
print("Can passenger {0:s} please go to flight {1:d}".format("Bianca",123))

age_groups = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
del age_groups [4]
print(age_groups)

hello_x_2=2
if (hello_x_2 == 2):
    print(hello_x_2)

print("Hello World".count('o', 5, 7))
my_s = "the rain in Spain, stays, mainly in the plain"
result_list = [my_s.split(',',1)[0]]
print(result_list)


# Counter class
sentence_1 = {"You", "used", "to", "love", "cake", "but", "now", "you",  "don\'t"}
sentence_2 = {"We", "used", "to", "enjoy", "cake", "but", "now", "we", "don\'t"}

from collections import Counter
def get_letter_freq(sentence_1):
     return Counter(sentence_1)

def get_letter_freq2(sentence_2):
    return Counter(sentence_2)

print("All words in both sentences :{}".format(sentence_1.union(sentence_2)))
print("Common words in both sentences :{}".format(sentence_1.intersection(sentence_2)))
print("Words that are not common to both sentences :{}".format(sentence_1.symmetric_difference(sentence_2)))






