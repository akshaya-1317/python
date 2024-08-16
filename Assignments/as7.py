#5. Write a program to find maximum of three numbers without using logical operators. You may use nested if-else statements.
#using logical operator
#using short-hand ifelse

#using if-else
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

if(num1 > num2) and (num1 > num3):
    print("Max number= ", num1)
elif(num2 > num1) and (num2 > num3):
    print("Max number= ", num2)
else:
    print("Max number= ", num3)


#using short-hand if-else
print("num1") if num1>num2 and num1>num3 else print("num2") if num2>num1 and num2>num3 else print("num3")


