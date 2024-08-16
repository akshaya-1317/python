def print_info1(name, age, addr, email):
    print("name =", name)
    print("age =", age)
    print("addr =", addr)
    print("email =", email)

## fn call -- args by default positional
# print_info1("James Bond", 60, "London", "james@bond.com")
## fn call -- args by name/keyword (arg sequence doesn't matter)
# print_info1(name="Superman", email="superman@gmail.com", addr="Crypton", age=65)


def print_info2(name, age, addr, email, /):
    print("name =", name)
    print("age =", age)
    print("addr =", addr)
    print("email =", email)


## fn call -- args by default positional
# print_info2("James Bond", 60, "London", "james@bond.com")
## Error: fn call cannot be done with named params due to /
# print_info2(name="Superman", email="superman@gmail.com", addr="Crypton", age=65)


def print_info3(*, name, age, addr, email):
    print("name =", name)
    print("age =", age)
    print("addr =", addr)
    print("email =", email)


## fn call -- args by name/keyword (arg sequence doesn't matter)
# print_info3(name="Superman", email="superman@gmail.com", addr="Crypton", age=65)
## Error -- cannot pass position params due to *
# print_info3("James Bond", 60, "London", "james@bond.com")


def print_info4(name, age, /, *, addr, email):
    print("name =", name)
    print("age =", age)
    print("addr =", addr)
    print("email =", email)


# first two params are positional due to /
# last two params are keyword/named due to *
print_info4("James Bond", 60, addr="London", email="james@bond.com")