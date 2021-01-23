name = "Robert"


def print_name():
    # local space
    name = "Csaba"


def print_another_name():
    name = "Kriszta"


def print_global_name():
    print(name)


def override_global_name():
    global name
    name = "Edina"


print(name)
override_global_name()
print(name)