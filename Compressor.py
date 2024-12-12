import os
from PIL import Image
import random as r


def get_size_format(b, factor=1024, suffix="B"):

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def random():

    string_random = ""

    for i in range(10):

        string_random += str(r.randint(0, 100))

    return string_random


def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    img = Image.open(image_name)
    image_size = os.path.getsize(image_name)

    if new_size_ratio < 1.0:
        img = img.resize(
            (int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)

    elif width and height:
        img = img.resize((width, height), Image.LANCZOS)
    filename, ext = os.path.splitext(image_name)
    if to_jpg:
        new_filename = f"{filename}_compressed_{random()}.jpg"
    else:
        new_filename = f"{filename}_compressed_{random()}{ext}"

    try:
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:
        img = img.convert("RGB")
        img.save(new_filename, quality=quality, optimize=True)
    new_image_size = os.path.getsize(new_filename)

    return {
        "image": new_filename,
        "size_before": get_size_format(image_size),
        "size_after": get_size_format(new_image_size),
        "size_change": f"{(new_image_size - image_size) / image_size*100:.2f}%"

    }
