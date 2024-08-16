# Create student class that takes name & marks of 3 subjects as arguments in constructor.
#Then create a method to print the average


# class student:
#
#     def __init__(self, name, m1, m2, m3, average):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.average = average
#
#     def avg(self):
#
#         m1 = int(input("Marks of 1st sub: "))
#         m2 = int(input("Marks of 2nd sub: "))
#         m3 = int(input("Marks of 3rd sub: "))
#         average = (m1+m2+m3)/3
#
#
# s1 = student()
# print(s1.avg)


#-----------------------------------------------------


class student:

    def __init__(self, name, marks):
         self.name = name
         self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum = sum+val
        print("hey", self.name, "Your avg score is:", sum/3)


s1 = student("ABC", [97,96,95])
s1.get_avg()
