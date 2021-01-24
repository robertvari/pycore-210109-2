import os


def find_all_files(root_folder, file_list, ext=None):
    folder_content = [os.path.join(root_folder, i) for i in os.listdir(root_folder)]

    if ext:
        file_list += [i for i in folder_content if os.path.isfile(i) and i.lower().endswith(ext)]
    else:
        file_list += [i for i in folder_content if os.path.isfile(i)]

    subfolders = [i for i in folder_content if os.path.isdir(i)]

    for f in subfolders:
        find_all_files(f, file_list)