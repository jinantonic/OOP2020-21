# Create base class
class Student:
    def __init__(self):
        
        # Protected member
        self.a = 'Jina'
        self.b = 'OOP'
    
    def course(self):
        print(self.a  + " listens to " + self.b + " lecture now")

    def enrollment(self):
        print(self.a  + " is a student now")

# Create derived class
class De_Student(Student):
    def __init__(self):

        # Call the constructor of the base class
        Student.__init__(self)
        print("Calling the protected member's name of the Student class :")
        print(self.a)

        Student.enrollment(self)
        print(self.a)

        Student.course(self)
        print(self.b)


student1 = De_Student()
student2 = Student()

# Call the protected member's name
print(student2.a)
print(student2.b)