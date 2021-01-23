def main_func():
    name = "Robert"
    print(name)

    def inner_func():
        name = "Csilla"
        print(name)

    inner_func()


main_func()