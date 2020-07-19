import requests

from utilites import load_image, get_file_extension


def fetch_hubble_launch(id_image, folder='./'):
    response = requests.get(f'http://hubblesite.org/api/v3/image/{id_image}')
    response.raise_for_status()
    extra_file = response.json()['image_files'][-1]
    url = f"https:{extra_file['file_url']}"
    path_file = f'{folder}/{id_image}{get_file_extension(url)}'
    load_image(url, path_file)


def load_collection_hubble(collection, folder='./'):
    response = requests.get(f'http://hubblesite.org/api/v3/images/{collection}/')
    response.raise_for_status()
    for image in response.json():
        fetch_hubble_launch(image['id'], folder)


if __name__ == '__main__':
    load_collection_hubble('printshop', 'images')
