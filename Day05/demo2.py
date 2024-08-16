
def function1():
    print("Inside, function1()...")


function1()
function2 = function1()

#function2()

print("type of function1 :", type(function1))
print("type of function2 :", type(function2))
print("name of fun : ", function1.__name__)
print("name of fun : ", function1.__name__)