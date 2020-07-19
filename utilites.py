import os
from pathlib import Path

import requests
from PIL import Image


def load_image(url, path_file):
    response = requests.get(url)
    response.raise_for_status()
    path = Path(path_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'bw') as file:
        file.write(response.content)


def get_file_extension(filename):
    return os.path.splitext(filename)[1]


def resize_image(path_image):
    converted_extension = ('PNG', 'TIFF')
    image = Image.open(path_image)
    if max(image.size) > 1080:
        image.thumbnail((1080, 1080))
        path_image_not_extension = os.path.splitext(path_image)[0]
        if image.format in converted_extension:
            image = image.convert('RGB')
        image.save(f'{path_image_not_extension}.jpg', format="JPEG")
    return f'{os.path.splitext(path_image)[0]}.jpg'
