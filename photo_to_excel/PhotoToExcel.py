from my_modules.my_functions import get_root_path, get_photo_files


def main():
    # get root path and validate it
    root_folder = get_root_path()

    # list jpg files in path
    photos = get_photo_files(root_folder)


if __name__ == '__main__':
    main()