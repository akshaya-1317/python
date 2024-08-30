

#Abstraction - Hide the implementation details of a class and show only the essential features.
#Encapsulation - Wrapping data and functions into single unit
#Inheritance -
#Polymorphism -

#class, objects, constructor, attributes, methods

#class
#constructor
#methods
#objects


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


#-------------------------------------------------

#static method - Don't use self parameter, works at class level not at object level.

class student:
    @staticmethod       #this is called decorator
    def college():
       print("ABC College")

#-------------------------------------------------


#del keyword: delete

class student:
    def __init__(self,name):
        self.name = name

s1 = student("pqr")
#print(s1.name)

del s1           #deletes s1
#print(s1.name)   #gives error

#-----------------------------------------

#private(like) attributes and methods
#uses double underscore e.g. __name then it becomes private.
#those Private attributes only can be accessible within class and in methods present in class not out of class or not after object.

class person:
    __name = "ABC"

    def __hello(self):
        print("this is private function!")

    def welcome(self):
        self.__hello()


p1 = person()
print(p1.welcome()) #welcome method is not private so it can be accessed here.

#-------------------------------------------------

#INHERITANCE - when one class(child) derives properties & methods of another class(parent)

class Car:      #parent class
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):  #got features of Car class.  #child class
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car2.start())

#-----------------------------------------------------

#Single Inheritance  --> base class(parent) --> Derived child class
#Multi-level Inheritance --> base class(parent) --> child class --> child class
#Multiple Inheritance

#Multi-level -->

class Car:      #parent class
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("diesel")
Car.start()

#-----------------------------------------

#Multiple Inheritance -- one derived class can inherit properties from many base class.

class A:
    varA = "this is class A"

class B:
    varB = "this is class B"

class C(A,B):
    varC = "this is class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

#---------------------------------------------
#Super -- Used to acsess methods of parent class
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started:")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = ToyotaCar("prius", "electric")
print(car1.type)

#------------------------------------------------------

#class method - bound to the class and receives the class as an implicit first argument.
# used to change class attributes.

class Student:
    @classmethod
    def college(cls):
        pass

#------------------------------------------------------

class Person:
    name = "ABC"  #To change this class attribute there are many ways


#way1:
#    def changeName(self,name):  #both names will be different abc, pqr
#       self.name = name

#way2:
    def changeName(self,name):   #both names will be as per class name pqr pqr
        Person.name = name

#way3:
    def changeName(self, name):
        self.__class__.name = "DEF"

#way4:
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("PQR")
print(p1.name)
print(Person.name)

#--------------------------------------------

#static methods
#class methods (cls)
#Instance method(simple methods) (self)

#@getter, @setter - to learn.

#--------------------------------------------
#@property
#property decorator

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stud1 = Student(99,98,97)
print(stud1.percentage)

stud1.phy = 90
print(stud1.percentage)

#------------------------------------------------

#polymorphism - many forms  :
#operator overloading
#when same operator is allowed to have different meaning according to the context.

#operators                  #dunder fun
# a+b       addition        a.__add__(b)
# a-b       subtraction     a.__sub__(b)
# a*b       multiplication  a.__mul____(b)
# a/b       division        a.__truediv____(b)
# a%b       addition        a.__mod____(b)

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def showNumber(self):
        print(self.real,"i +", self.imag,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)

num1 = Complex(4,6)
num1.showNumber()

num2 = Complex(5,8)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()


