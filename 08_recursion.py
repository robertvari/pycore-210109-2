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

    file_list += [i for i in folder_content if os.path.isfile(i)]

    subfolders = [i for i in folder_content if os.path.isdir(i)]

    for f in subfolders:
        find_all_files(f, file_list)


file_list = []
find_all_files("D:\\Photos", file_list)
for i in file_list:
    print(i)
# print(len(file_list))