# behaviours
class MyDogs:
    def bark(self):
        print('wuff wuff')

rex = MyDogs()
rex.bark()

# functions
def hello_world(say_something):
    return say_something

print("We say: ", hello_world("I love programming"))

# 여기

# scope
# global scope
greeting = "Hello World"

def change_greeting(new_greeting):
    greeting = new_greeting # new variable is created

def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()

# the global keyword
greeting = "Hello World"

def change_greeting(new_greeting):
    global greeting
    greeting = new_greeting

def greeting_world():
    world = "World"
    print(greeting, world)

change_greeting("Hi")
greeting_world()

# enclosing scope
def outer():
    first_num = 1

    def inner():
        first_num = 0 # trying to change the value of first_num to 0 inside of inner(), which is not working
        second_num = 1
        print("inner - second_num is:", second_num)

    inner()
    print("outer - first_num is:", first_num)
outer()

# enclosing scope - the nonlocal keyword
def outer():
    first_num = 1

    def inner():
        nonlocal first_num # forces the variable to go one higher up in the scope
        first_num = 0
        second_num = 1
        print("inner - second_num is:", second_num)

    inner()
    print("outer - first_num is:", first_num)
outer()

# class instance vs class attribute
import datetime

class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, f_name, l_name):
        if title not in self.TITLES:
            raise ValueError("Not a valid title: ", title)

        self.title = title
        self.firstname = f_name
        self.lastname = l_name

        today = datetime.datetime.now().strftime("%A")
        if today == "Wednesday":
            print(today)

p = Person("Ms", "Jina", "Park")
print(p.TITLES)
print(Person.TITLES)
print(p.firstname)

class Person:
    def __init__(self):
        self.name = 'Jina'
        self.age = 4

    def get_age(self):
        print(self.name, "is", self.age, "years old")

p = Person()
p.get_age()

class Student(Person):
    def __init__(self):
        self.studentID = 1234

    def enrol_into_uni(self):
        print("I am a student now")

    def get_studentID(self):
        print("My student ID is:", self.studentID)

s = Student()
s.get_studentID()

class Person:
    def init(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        print(self.name, "is", self.age, "years old")

p = Person()

class Student(Person):
    def init(self, name, age, studentID): # Have to call the parent init because the attribute wasn't set
        self.studentID = studentID
        super().init(name, age)

    def enrol_into_uni(self):
        print("I am a student now")

    def get_studentID(self):
        print("My student ID is:", self.studentID)

s = Student()
s.init("Jina", 5, 1234)
s.enrol_into_uni()
s.get_age()
s.get_studentID()

# multiple inheritance
# case 1 : method overriden in all parent classes
class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    def play_game(self):
        print("Playing in ClassB")

class ClassC(ClassA):
    def play_game(self):
        print("Playing in ClassC")

class ClassD(ClassB, ClassC): # the output depends on which class is mentioned first in the brackets
    pass

d = ClassD()
d.play_game()

# case 2 : method overriden in some parent classes
class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    pass # 아무것도 실행하지 않고 다음 행으로 넘어감

class ClassC(ClassA):
    def play_game(self):
        print("Playing in ClassC")

class ClassD(ClassB, ClassC): # the output depends on which class is mentioned first in the brackets
    pass

d = ClassD()
d.play_game()

# case 3 : method overriden in all classes
class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    def play_game(self):
        print("Playing in ClassB")

class ClassC(ClassA):
    def play_game(self):
        print("Playing in ClassC")

class ClassD(ClassB, ClassC): # the output depends on where tge furst mention in the mro is of this method (D -> B -> C)
    def play_game(self):
        print("Playing in ClassD")

d = ClassD()
d.play_game()

# case 4 : calls to super()
class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    def play_game(self):
        print("In ClassB")
        super().play_game() # class A는 super()을 이용해 부모의 play_game()을 호출

class ClassC(ClassA):
    def play_game(self):
        print("In ClassC")
        super().play_game()

class ClassD(ClassB, ClassC):
    def play_game(self):
        print("Playing in ClassD")
        super().play_game()

d = ClassD()
d.play_game()

class ClassA:
    def play_game(self):
        print("Playing in ClassA")

class ClassB(ClassA):
    def play_game(self):
        print("In ClassB")
        super().play_game() # class A는 super()을 이용해 부모의 play_game()을 호출

# multiple inheritance, control who's next in line with explicit cells
class ClassC(ClassA):
    def play_game(self):
        print("In ClassC")
        super().play_game()

class ClassD(ClassB, ClassC):
    def play_game(self):
        print("Playing in ClassD")
        ClassA.play_game(self)

d = ClassD()
d.play_game()

# case 5
class X:
    pass
class Y:
    pass
class Z:
    pass
class A(X, Y):
    pass
class B(Y, Z):
    pass
class M(B, A, Z):
    pass

print(M.mro())

# composition
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.salary_object = Salary(pay, bonus)

    def total_salary(self):
        return self.salary_object.annual_salary()

e = Employee("Jina", 25, 2500, 10000)
print(e.total_salary())

# aggregation
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary_object = salary

    def total_salary(self):
        return self.salary_object.annual_salary()

s = Salary(2500, 10000) # instantiationg Salary as a seperate, independent class
e = Employee("Jina", 25, s)
print(e.total_salary())

# different methods
class DifferentMethodsClass:
    class_attribute = "This is a class attribute"

    def __init__(self):
        self.instance_attributes = "This is an instance attribute"

    def instance_method(self): # usual argument self
        print('instance method called', self)

    @classmethod
    def class_method(cls): # notice what's new in the argument list
        print('class method called', cls)
        #print(self.instance_attributes) # this will fail
        print("class attribute: ", cls.class_attribute)

    @staticmethod
    def static_method(): # notice nothing in the argument list
        print('static method called')

demo = DifferentMethodsClass()
demo.instance_method()
demo.class_method() # does not have access to instance variables
demo.static_method()
DifferentMethodsClass.class_method()
DifferentMethodsClass.static_method()
#DifferentMethodsClass.instance_method() # error

# static method
import math # 모듈 불러옴
class Pizza:
    def __init__(self, ingredients, pizza_size = 3):
        self.ingredients = ingredients
        self.pizza_size = pizza_size
        print("in init")

    def __str__(self):
        return f'Pizza({self.ingredients}) of size: {self.pizza_size}'

    # add some class methods
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    @staticmethod
    def pizza_area(r):
        return r ** 2 * math.pi

pizza = Pizza(['cheese', 'tomatoes'])
print(pizza)
print(Pizza.prosciutto())
print(Pizza.margherita())
#print(Pizza.ingredients) # cause an error, cannot access instance variables
print(Pizza.pizza_area(3))

# abstract class
from abc import ABC, abstractmethod
class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):
    def no_of_sides(self): # overriding abstract method
        print("I have 3 sides")

t = Triangle()
t.no_of_sides()

class Pentatgon(Polygon):
    def no_of_sides(self): # overriding abstract method
        print("I have 5 sides")

p = Pentatgon()
p.no_of_sides()


# call to super()
class Polygon(ABC):

   @abstractmethod
   def no_of_sides(self):
       pass

   def what_am_I(self):
       print("I am a parent Polygon")

class Triangle(Polygon):
   def no_of_sides(self): # overriding abstract method
       print("I have 3 sides")

   def what_am_I(self):
       print("I am a Triangle child class")
       super().what_am_I()

t = Triangle()
t.no_of_sides()
t.what_am_I()

# abstract classes can have abstract methods and
# abstract properties
class Polygon(ABC):

   @abstractmethod
   def no_of_sides(self):
       pass

   def what_am_I(self):
       print("I am a parent Polygon")

   @property
   @abstractmethod # the abstract decorator should be the last one in the list
   def length(self):
       pass

class Triangle(Polygon):

   def __init__(self):
       self.__x = 0

   def no_of_sides(self):
       print("I have 3 sides")

   def what_am_I(self):
       print("I am a Triangle child class")
       super().what_am_I()

   @property
   def length(self):
       return self.__x

   @length.setter
   def length(self, value):
       self.__x = value


# print(Triangle.__mro__)
t = Triangle()
t.no_of_sides()
print(t.length)
t.length = 5
print(t.length)

# polymorphism
class Cat:
   def makeSound(self):
       print("meow")

class Dog:
   def makeSound(self):
       print("wouff wouff")

def speak(animalType):
   animalType.makeSound()

cat = Cat()
dog = Dog()
speak(cat)
speak(dog)

# testcase
import unittest
#class CheckNumbers(unittest.TestCase): # first subclass from TestCase
#    def test_int_test_float(self): # Test_int_test_float checks and either raises an exception or succeed depending on if the w parameters are equal
#        self.assertEqual(1, 1.0)

#    def test_int_test_float(self):
#        self.assertEqual(1, 1.0)


#if __name__ == "__main__":
#    unittest.main()

# setUp()
#class StatsList(list):
#    def mean(self):
#        return sum(self)/len(self)

#    def median(self):
#        if len(self)%2:
#            return self[int(len(self)/2)]
#        else:
#            idx = int(len(self)/2)
#            return (self[idx] + self[idx - 1])/2

#    def mode(self):
#        freqs = defaultdict(int)
#        for item in self:
#            freqs[item] += 1

#        mode_freq = max(freqs.values())
#        modes = []

#        for item, value in freqs.items():
#            if value == mode_freq:
#                modes.append(item)

#        return modes

# tests can be executed in any order and the result of one does not influence the other
#class TestValidInputs(unittest.TestCase):
#    def setUp(self): # setUp() is called individually before each test
#       self.stats = StatsList([1,2,2,3,3,4])

#    def test_mean(self):
#       self.assertEqual(self.stats.mean(), 2.5)

#    def test_median(self): # alters the list
#        self.assertEqual(self.stats.median(), 2.5)
#        self.stats.append(4)
#        self.assertEqual(self.stats.median(), 3)

#    def test_mode(self):
#        self.assertEqual(self.stats.mode(), [2,3])
#        self.stats.remove(4)
#        self.assertEqual(self.stats.mode(), [3])

#if __name__ == "__main__":
#    unittest.main()

    # Iterator Example

# iterate over something in Python
my_numbers = (1, 2, 3, 4, 5)

# "under the hood" there's a design pattern at work
for number in my_numbers:
    print(number)

# doing the same as before, but now
# explicitly calling the iterator
it = iter(my_numbers)
print(next(it))
print(next(it))
print(next(it))

# or with loop
# experiment with this. For example, run it to a certain number and then start a loop again, how does it behave compared to doing the same in a for loop
while True:
    try:
        number = next(it)
    except StopIteration:
        break
    else:
        print(number)


# iterating over a file preserves state
#def parse_email(f):
#    envelope = ''
#    for line in f:
#        envelope.join(line)
#        break
#    headers = {}
#    for line in f:
#        if line == '\n':
#            break
#        name, value = line.split(':', 1)
#        headers[name.strip()] = value.lstrip().rstrip('\n')
#    body = []
#    for line in f:
#        if line.startswith('From'):
#            break
#        body.append(line)
#    return envelope, headers, body
#with open("email.txt") as f:
#    envelope, header, body = parse_email(f)
#print(body)

# make your own iterator with your own objects:
# 1. an iterable class: create iterator object
class OddIterator():
   def __init__(self, container):
       self.container = container
       self.n = -1

   def __next__(self):
       self.n += 2
       if self.n > self.container.maximum:
           raise StopIteration

       return self.n

   def __iter__(self):
       return self

# 2. an iterator class: traverse the container
class OddNumbers:
   def __init__(self, maximum):
       self.maximum = maximum

   def __iter__(self):
       return OddIterator(self)

numbers = OddNumbers(7)

for number in numbers:
   print(number)

it = iter(OddNumbers(5))
print(next(it))
print(next(it))
print(list(numbers))
print(set(n for n in numbers if n > 4))

# First: prep for Singleton: What is __new__
class A():
   def __new__(cls):
       print("Creating instance")
       return super(A, cls).__new__(cls)

   def __init__(self):
       print("Init is called")

a = A()

class Singleton:
   def __new__(cls):
       if not hasattr(cls, 'instance'):
           cls.instance = super(Singleton, cls).__new__(cls)
       return cls.instance

s = Singleton()
print("Object created:", s)
s1 = Singleton()
print("Object created:", s1)

# Singleton solved with decorator
class Singleton:
   def __init__(self, cls):
       self._cls = cls

   def Instance(self):
       try:
           return self._instance
       except AttributeError:
           self._instance = self._cls()
           return self._instance

   def call(self):
       raise TypeError

   def __instancecheck__(self, instance):
       return isinstance(instance, self._cls)

@Singleton
class DBConnection:
   def __init__(self):
       print("established db connection")

   def __str__(self):
       return "Database connection object"

#db_con = DBConnection()   #causes the TypeError
db_connection1 = DBConnection.Instance()
db_connection2 = DBConnection.Instance()

print(f"ID of connection 1: {id(db_connection1)}")
print(f"ID of connection 2: {id(db_connection1)}")

# decorators
# function revision:
def say_name():
   print("Jina")

def say_nationality():
   print("Korean")

def say(function):
   return function

say(say_name)()
say(say_nationality)()

# now with an inner function
# output will be the same
def say():

   def say_name():
       print("Jina")

   def say_nationality():
       print("Korean")

   say_name()
   say_nationality()

say()

# now make it a decorator
def say(func):
   def say_name():
       print("Jina")

   def say_nationality():
       print("Park")

   def wrapper():
       say_name()
       say_nationality()
       func()

   return wrapper

@say
def start_example():
   print("In the example")

start_example()
# when the start_example is called, it goes straight to the say() function and defines say_name() and say_nationality()
# and the wrapper() function and finally returns the wrapper

# an implementation of a facade pattern
# the complex system
class Cutter:

   def cut_vegetables(self):
       print("Cutting veggies!")

class Boiler:

   def boil_vegetables(self):
       print("Boiling veggies!")

class Frier:

   def fry_vegetables(self):
       print("Frying veggies!")

# the facade easy interface
class Cook:

   def prepare_dish(self):
       self.my_cutter = Cutter()
       self.my_cutter.cut_vegetables()

       self.my_boiler = Boiler()
       self.my_boiler.boil_vegetables()

       self.my_frier = Frier()
       self.my_frier.fry_vegetables()

my_cook = Cook()
my_cook.prepare_dish()



