#define Employee class with attributes - role, dept, salary
#the class also has showDetails() method
#create Engineer class which inherit properties from employee and has additional attributes name and age.

class Employee:

    def __init__(self, rollNo, dept, salary):
        self.rollNo = rollNo
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("roll No.", self.rollNo, "department", self.dept, "Salary", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age



emp1 = Employee(1, "Physics", 80000)
emp1 = Engineer("ABC", 20)

print(emp1.showDetails())

