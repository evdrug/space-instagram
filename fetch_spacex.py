import requests

from utilites import load_image


def fetch_spacex_last_launch(folder='./'):
    response = requests.get('https://api.spacexdata.com/v4/launches/latest')
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for i, url in enumerate(images, start=1):
        load_image(url, f'{folder}/spacex{i}.jpg')


if __name__ == '__main__':
    fetch_spacex_last_launch('images')
