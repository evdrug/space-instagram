# Космический Инстаграм
Публикация фотографий в Инстаграм

## Как установить
    
    1.Переименовать файл  .env.example в .env
    
    2.Добавить учетный данные от аккаунта instagram в файл .env 
    
    3.Python3 должен быть уже установлен. 
        Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
   
        pip install -r requirements.txt
    
## Как пользоваться
Загрузка фотографий с последнего запуска SpaceX
    
    python fetch_spacex.py
    
Загрузка картинок от Hubble

    python fetch_hubble.py
    
Публикация в инстаграм

    python instagram_publication_photos.py


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков https://dvmn.org.