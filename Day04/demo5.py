
# default params i.e. params with default values.
#   if param is not passed while calling, then default value will be taken
def print_info(name, age, addr="Pune", email="unknown@gmail.com"):
    """
    prints info about a person.

    :param name: string
    :param age: int
    :param addr: string
    :param email: string
    :return:
    """
    print("name =", name)
    print("age =", age)
    print("addr =", addr)
    print("email =", email)

def function1():
    print("------------")




print_info(name="James Bond", age=60)
function1()
print_info("Superman", 65, "Crypton", "s@g.com")
function1()
print_info("Spiderman", 45, "USA")
function1()