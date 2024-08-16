#3. Input a 4 digit int from user and print sum of its digits.


sum = 0
number = input("Enter a 4 digit number: ")

for x in str(number):
    sum = sum + int(x)

print("sum of digits: ", sum)

