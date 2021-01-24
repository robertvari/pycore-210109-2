import os


def get_root_path():
    user_input = input("Root folder:")
    assert os.path.exists(user_input), f"Path {user_input} does not exist."

    return user_input


def get_photo_files(folder_path):
    photo_list = [
        os.path.join(folder_path, photo) for photo in os.listdir(folder_path)
        if photo.lower().endswith(".jpg")
    ]

    return photo_list