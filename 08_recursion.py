import os


def get_factorial(n):
    if n < 2:
        return n
    else:
        return n * get_factorial(n-1)

# result = get_factorial(5)
# print(result)


def find_all_files(root_folder, file_list):
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]
    pass

file_list = []
find_all_files("D:/Photos", file_list)
print(file_list)