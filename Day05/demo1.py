def fun():
    print("------------------------")


def function():
    pass              #This is empty function.

function()
fun()



def outer_fun1():
    def inner_fun1():
        print ("This is inner fun1")

    inner_fun1()
    print("Inside outer_fun1 and outside inner_fun1")
outer_fun1()
fun()



def outer_fun2():
    global inner2_fun # to check the scope of global var
    def inner_fun2():
        print("This is inner_fun2")

    inner_fun2()
    print("Inside outer_fun2 and outside inner_fun1")
outer_fun2()




number3 = 100 # global var
def outer_fun3():
    num3 = 200 # local var
    def inner_fun3():
        print("this is inner fun3")
        print("global var = ", number3)
        print("local var = ", num3)
        n3 = 300
        print("changed n3 = ", n3)

    inner_fun3()
outer_fun3()
fun()










