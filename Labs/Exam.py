# iterate over a file
fo = open('plaintext.txt', 'r')
print(fo.read())

fo = open('plaintext.txt', 'r')
for line in fo:
    print(line)

#fo = open('plaintext.txt', 'r')
#for line in fo:
#    line = line.splitlines()
#print(line)


# iterate over a list
list = ['cat', 'dog', 'lion', 'zerba', 'flamingo']
for i in list:
    print(i)

for index, number in enumerate(list):
    print(index, number)

# Format a string in a print() function to display 
# the number 12 with 10 leading space characters
str = "12"
print(str + 10 * ' ')
print(str.rjust(10))
print(str.ljust(10))
print('%10d'%(12))

# True or false
print('123'.isdigit())
print('123abc'.isdigit())
print('abc'.isdigit())
print('1 2 3'.isdigit())
print('1 2 3'.isalpha())

# Listing 1(a)
"""my_input = input('tell me a letter between a and c >')

if my_input == 'a':
    print("a was input")
elif my_input == 'b':
    print("b was input")
elif my_input == 'c':
    print("c was input")
else:
    print("wrong letter, sorry.")"""

# Listing 1(b)
"""my_input = input('tell me a letter between a and c >')

if(my_input == 'a'):
    print("a was input")
if(my_input == 'b'):
    print("b was input")
if(my_input == 'c'):
    print("c was input")
else:
    print("wrong letter, sorry.")"""


# Inheritance
class Animal:
    def __init__(self):
        self.type = 'Cat'
        self.name = 'Ovid'
        self.age = 7

    def get_info(self):
        print(self.type + ' ' + self.name, "is", self.age, "years old.")

p = Animal()
p.get_info()

class Pet(Animal):
    pass

s = Pet()
s.get_info()

# Composition
class VetFee:
    def __init__(self, pay, extra):
        self.pay = pay
        self.extra = extra

    def annual_fee(self):
        return (self.pay * 12) + self.extra

class Owner:
    def __init__(self, petName, petAge, pay, extra):
        self.petName = petName
        self.age = petAge
        self.VetFee_object = VetFee(pay, extra)

    def total_fee(self):
        return self.VetFee_object.annual_fee()

e = Owner("Ovid", 7, 5000, 100000)
print(e.total_fee())

# Decorator
def say(func):
    def say_name():
        print("Jina")

    def say_nationality():
        print("Korean")
    
    def wrapper():
        say_name()
        say_nationality()
        func()
    
    return wrapper

@say
def start_example():
    print("In the example")

start_example()

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass

class Concrete_Coffee(Coffee):
    def get_cost(self):
        return 3.5

class decorator_coffee(Coffee):
    def __init__(self, dec_coffee):
        self.dec_coffee = dec_coffee
    
    def get_cost(self):
        return self.dec_coffee.get_cost()
    
class coffee_with_milk(decorator_coffee):
    def __init__(self, dec_coffee):
        decorator_coffee.__init__(self, dec_coffee)

    def get_cost(self):
        return self.dec_coffee.get_cost() + 0.5

class coffee_with_almond_milk(decorator_coffee):
    def __init__(self, dec_coffee):
        decorator_coffee.__init__(self, dec_coffee)
    
    def get_cost(self):
        return self.dec_coffee.get_cost() + 1.0

import exam

c = exam.Concrete_Coffee()
print(c.get_cost())

class Student:
    def __init__(self, name):
        self.name = name
    
    def print_my_name(self):
        print("My name is ", self.name)

student_1 = Student("Bianca")
student_1.print_my_name()



class Animal:
    def __init__(self):
        self.type = 'Cat'
        self.name = 'Ovid'

    def get_info(self):
        print("This is a " + self.type + " named " + self.name)

a = Animal()
a.get_info()

class Owner(Animal):
    def __init__(self):
        self.age = 7
    
    def get_age(self):
        print(a.type + ' ' + a.name + " is", self.age, "years old.")

o = Owner()
o.get_age()
