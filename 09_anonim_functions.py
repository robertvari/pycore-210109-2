my_lambda = lambda a, b: a+b
# print(my_lambda(3, 3))

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna"]

# print(sorted(name_list))

print(sorted(name_list, key=lambda name: name.split(" ")[-1]))