
num=100 #Global var


def fun1():
   # print("fun1 = ", num ) #called global variable
    num = 200
    print("fun1 = ", num) #called 200


def fun2():
    global num
    num = 300
    print("fun2 is = ", num) #300 overrides over global variable


def fun3():
    global name
    name = "Sunbeam"
    print("fun3 = ", name)


fun1()
fun2()
fun3()