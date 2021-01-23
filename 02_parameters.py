import os


def list_directory(root_path):
    print(os.listdir(root_path))


# required positional arguments
def say_hello(name, age):
    print(f"Hello {name}. You are {age} old.")


# say_hello("Robert", 32)
# say_hello(age=32, name="Robert")

# default parameters
def add_numbers(a=0, b=0):
    print(a + b)


def register_user(email, password, address=None, phone=None):
    print(f"User email: {email}")
    print(f"User password: {password}")
    print(f"User address: {address}")
    print(f"User phone: {phone}")
# register_user("robert@gmail.com", "testpas123", address="Budapest")

# arbitrary number arguments
def print_all_params(*args):
    for i in args:
        print(i)
# print_all_params("Robert", "Budapest", 3.14, ["apple", "banana"], True)