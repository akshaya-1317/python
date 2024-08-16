# Input marks for 5 sub and calculate average
# a,b,c,d,e = input("Enter 5 values : ").split()
# print("marks of a = ", a)
# print("marks of b = ", b)
# print("marks of c = ", c)
# print("marks of d = ", d)
# print("marks of e = ", e)

num = int(input('How many numbers you want : '))
total_sum = 0

for n in range(num):
    numbers = float(input('Enter numbers : '))
    total_sum += numbers

    avg = total_sum/num
    print('Average of ', num, 'number is: ', avg)
