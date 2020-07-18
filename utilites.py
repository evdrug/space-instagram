import requests
from pathlib import Path
from PIL import Image, UnidentifiedImageError


def load_image(url, path_file):
    response = requests.get(url)
    response.raise_for_status()
    path = Path(path_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'bw') as file:
        file.write(response.content)


def file_extension(filename):
    return filename.rsplit('.', 1)[-1]


def resize_image(path_image):
    converted_extension = ('PNG', 'TIFF')

    try:
        image = Image.open(path_image)
    except UnidentifiedImageError:
        print(f"Error open file {path_image}")
        return None

    max_size = max(image.size)
    if max_size > 1080:
        difference = max_size / 1080
        image.thumbnail((int(image.width / difference), int(image.height / difference)))
        path_image_not_extension = path_image.rsplit('.', 1)[0]
        if image.format in converted_extension:
            image = image.convert('RGB')
        image.save(f'{path_image_not_extension}.jpg', format="JPEG")
