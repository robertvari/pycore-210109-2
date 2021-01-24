import os
from PIL import Image, ExifTags


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


def get_photo_data(file_path):
    img = Image.open(file_path)

    image_name = os.path.basename(file_path)
    image_size = f"{img.size[0]}x{img.size[1]}"

    image_data = {
        "Name": image_name,
        "Dimensions": image_size
    }

    exif_data = img._getexif()  # Sometimes None
    if not exif_data:
        return image_data

    for key, value in exif_data.items():
        tag_name = ExifTags.TAGS.get(key)
        if not tag_name:
            continue

        if tag_name == "DateTimeOriginal":
            image_data[f"Date"] = value

    return image_data


if __name__ == '__main__':
    image_data = get_photo_data("D:\\Photos\\CIW\\IMG_1100.JPG")
    print(image_data)