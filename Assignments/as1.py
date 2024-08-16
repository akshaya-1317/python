# Input marks of 5 subjects and calculate its average.


# marks = []
# total_marks = 0
#
# x = int(input("Enter 5 numbers: "))
#
# for i in range(5): # Get 5 numbers
#    marks.insert(i, x)
#
# for i in range(5): # Add numbers
#     total_marks = total_marks + marks[i]
#
# average = total_marks/5
# print("Average marks = ", average)


marks = []
total_marks = 0

print("Enter 5 subject marks: ")
for i in range(5): # Get 5 numbers
 #  print("Enter", i ,"number: ")
   marks.insert(i, int(input()))

for i in range(5): # Add numbers
    total_marks = total_marks + marks[i]

average = total_marks/5
print("Average marks = ", average)












