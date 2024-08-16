#
def function1(arg):
     print("argument = ", arg)
     print("type of args = ", type(arg))
     print("address of args = ", id(arg))


function1("abc") #indentation matters here.
function1("20")


# def function1(arg):
#     print("arg =", arg)
#     print("type of arg =", type(arg))
#     print("addr of arg =", id(arg))
#
#
# def print_line():
#     print("-" * 40)
#
#
# function1(123)
# print_line()
# function1(9.81)
# print_line()
# function1("Nilesh")
# print_line()
# function1(True)
# print_line()