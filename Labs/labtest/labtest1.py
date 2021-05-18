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


class stringCheck:

    def _init_(self):
        self.my_dict = self.create_dict()

    def create_dict(self):
        my_dict = {}
        # your code goes here:
        sen1 = "you used to love cake but now you don't"
        sen2 = "we used to enjoy cake but now we don't"

        list = sen1.split(" ")
        list2 = sen2.split(" ")
        list=list+list2
        list3=[]
        for i in list:
            my_dict = self.add_to_dict(i, my_dict)

        for i in my_dict:
            if my_dict[i] ==1:
                list3.append(i)

        print(list3)


        return my_dict

    def add_to_dict(self, key, the_dict):
        # your code goes here
        if key in the_dict:
            the_dict[key] = the_dict[key] + 1
        else:
            the_dict[key] = 1

        return the_dict

name=stringCheck()
name.create_dict()

class Person:
   def __init__(self, f_name, l_name):
     self.first_name = f_name
     self.last_name = l_name

   def print_name(self):
     print(self.first_name, self.last_name)

# Use the Person class to create an object, and then execute the printname method:

bsp = Person("Jina", "Park")
bsp.print_name()


# class Student(Person):
#   pass

# you have access to the methods and attributes
# of the parent class without having to
# program any of the functionality
# x = Student("John", "Doe")
# x.print_name()
# notice how we do not need an instance of Person
# in order to use the Student. The definition of
# Person was enough to be able to use it.

# now extend Student class with more functionality
# class Student(Person):
#   # init in Student overrides init from Person
#   def __init__(self, s_id, f_name, l_name):
#     self.student_id = s_id
#
#
# x = Student(12345, "John", "Doe")
# x.print_name() # causes an error if not defined in init

# now corrected student:
# class Student(Person):
#   # init in Student overrides init from Person
#   # super() grabs the class one higher in the hierarchy
#   # the parent class and initialises the fname and lname
#   def __init__(self, s_id, f_name, l_name):
#     super().__init__(f_name, l_name)
#     self.student_id = s_id
#
#
# x = Student(12345, "John", "Doe")
# x.print_name()
# print(x.student_id)