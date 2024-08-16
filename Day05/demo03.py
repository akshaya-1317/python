#ALIAS CONCEPT
def add(a,b):
    res = a + b
    print("Add() : ", a, "+", b, "=", res)


def subtract(a,b):
    res = a - b
    print("subtract() : ", a, "-", b, "=", res)


def multiply(a,b):
    res = a * b
    print("Multiply() : ", a, "*", b, "=", res)

#op will be Alias to pass function.
def calculate(x,y, op):
    print("In calculate()")
    op(x,y)

def Separate():
    print("--------------")

n1 = 10
n2 = 5
calculate(n1, n2, add)      #op is alias to add fun
calculate(n1, n2, subtract) #op is alias to sub fun
calculate(n1, n2, multiply) #op is alias to multiply fun
print()
                            #alias - we can pass fun as argument to another fun. such fun are called as higher order fun.
Separate()


ops = [add, subtract, multiply]
for op in ops:
    op(10,5)


