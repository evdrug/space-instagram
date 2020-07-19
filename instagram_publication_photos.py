import os

from dotenv import load_dotenv
from instabot import Bot

from utilites import resize_image


if __name__ == '__main__':
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    folder = 'images'

    bot = Bot()
    bot.login(username=login, password=password)
    for path in os.listdir(folder):
        if os.path.isfile(f'{folder}/{path}'):
            try:
                image_name = resize_image(f'{folder}/{path}')
            except Exception as e:
                print('Ошибка при обработке', path, e)
            else:
                if image_name:
                    bot.upload_photo(image_name, caption=image_name.replace(".jpg", ''))
                    if bot.api.last_response.status_code != 200:
                        print(bot.api.last_response)
