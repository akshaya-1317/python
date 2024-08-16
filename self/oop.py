
#class, objects, constructor, attributes, methods


#------------------------------------------

# class student():  #class created - blueprint of objects - features of object
#     name = "ABC"
#
# s1 = student()    #object created
# print(s1.name)

#-----------------------------------------

# class student:
#     name ="ABC"
#     def __init__(self):
#         print("adding new student")
#
# s1 = student()

#-----------------------------------------

class Student:

    def __init__(self, fullname, age):
        self.name = fullname
        self.age = age
        print("adding new student")

s1 = Student("ABC", 20)
print(s1.name, s1.age)

s2 = Student("DEF", 20)
print(s2.name, s2.age)

#---------------------------------------------


class Student:

    college_name = "xyz College"  #common for all students # this is class attribute
    #default constructors = even if we dont create it python will create it
    def __init__(self):  #we generally create only one constructor. so we don't write this.
        pass

    #parameterized constructor   # here object attributes are - name, age
    def __init__(self, fullname, age):
        self.name = fullname
        self.age = age
        print("adding new student")

s1 = Student("ABC", 20)
print(s1.name, s1.age, s1.college_name)

s2 = Student("DEF", 20)
print(s2.name, s2.age, s2.college_name)

#Also can be written as -->
#print(Student.college_name)

#----------------------------------------------------

# __init__ is a constructor method we can make more methods like below

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):  # more methods.
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks

s1 = student("karan", 98)
print(s1.name, s1.marks)
s1.welcome()
print(s1.get_marks())


