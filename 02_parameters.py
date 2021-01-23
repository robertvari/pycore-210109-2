import os


def list_directory(root_path):
    print(os.listdir(root_path))


# required positional arguments
def say_hello(name, age):
    print(f"Hello {name}. You are {age} old.")


say_hello("Robert", 32)
