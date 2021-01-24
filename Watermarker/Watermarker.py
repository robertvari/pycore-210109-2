import os, queue, threading
from PIL import Image, ImageDraw, ImageFont

job_queue = queue.Queue()


def main():
    folder_path = "D:\\Photos\\CIW"
    watermark_text = "Hello World"

    photo_files = get_photo_files(folder_path)

    for i in photo_files:
        job_queue.put({"path": i, "text": watermark_text})


def get_photo_files(folder_path):
    photo_list = [
        os.path.join(folder_path, photo) for photo in os.listdir(folder_path)
        if photo.lower().endswith(".jpg")
    ]

    return photo_list


def watermark_worker():
    while not job_queue.empty():
        job_data = job_queue.get()

        root_dir = os.path.dirname(job_data["path"])
        save_folder = os.path.join(root_dir, "_watermarked")
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        photo_path = job_data["path"]
        watermark_text = job_data["text"]

        image_name = os.path.basename(photo_path)
        img = Image.open(photo_path)
        img.thumbnail((800, 800))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 150)
        draw.text((0, 0), watermark_text, fill=(255, 0, 0), font=font)

        img.save(os.path.join(save_folder, image_name))


if __name__ == '__main__':
    main()