import os

from dotenv import load_dotenv
from instabot import Bot

from utilites import resize_image

FOLDER = 'images'
load_dotenv()
LOGIN = os.getenv('INSTAGRAM_LOGIN')
PASSWORD = os.getenv('INSTAGRAM_PASSWORD')


def optimize_photos():
    for file in os.listdir(FOLDER):
        if os.path.isfile(f'{FOLDER}/{file}'):
            resize_image(f'{FOLDER}/{file}')


if __name__ == '__main__':
    optimize_photos()

    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)
    for image in os.listdir(FOLDER):
        if image.endswith('.jpg'):
            bot.upload_photo(f'{FOLDER}/{image}', caption=image.replace(".jpg", ''))
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
