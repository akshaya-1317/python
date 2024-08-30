

num = int(input("Enter any number: "))
if num > 1:
 for x in range(2, num):

    if(num % x) == 0:
       print("number is not a prime number")
    else:
       print("number is the prime number")

else:
       print("not prime number")
