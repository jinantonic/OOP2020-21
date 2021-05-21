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
class Person:
    def __init__(self):
        self.name = 'Jina'
        self.age = 26

    def get_age(self):
        print(self.name, "is", self.age, "years old.")

p = Person()
p.get_age()

class Studnet(Person):
    pass

s = Studnet()
s.get_age()

# Composition
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary_object = Salary(pay, bonus)

    def total_salary(self):
        return self.salary_object.annual_salary()

e = Employee("Jina", 26, 5000, 100000)
print(e.total_salary())

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
