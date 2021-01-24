import os
from PIL import Image, ExifTags
from openpyxl import Workbook


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


def write_data_to_excel(root_folder, photo_data_list):
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Name"
    sheet["B1"] = "Date"
    sheet["C1"] = "Dimensions"

    for index, data in enumerate(photo_data_list):
        row = index + 3
        sheet[f"A{row}"] = data.get('Name')
        sheet[f"B{row}"] = data.get('Date')
        sheet[f"C{row}"] = data.get('Dimensions')

    excel_file = os.path.join(root_folder, "photo_data.xlsx")
    workbook.save(excel_file)


if __name__ == '__main__':
    photo_data_list = [{'Name': 'IMG_1069.JPG', 'Dimensions': '2592x1728', 'Date': '2016:08:20 09:19:06'}, {'Name': 'IMG_1070.JPG', 'Dimensions': '2592x1728', 'Date': '2016:08:20 09:19:20'}]
    write_data_to_excel("D:\\Photos\\CIW", photo_data_list)