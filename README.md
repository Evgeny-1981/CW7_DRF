Курсовая работа по DRF. Трекер полезных привычек.

Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 



Запуск проекта.

1. Клонируйте проект 
        
        git clone git@github.com:Evgeny-1981/CW7_DRF.git
                        
2. Создайте виртуальное окружение

        python3 - m venv .venv
3. Установите зависимости виртуального окружения 

        poetry install
4. Переименуйте файл .env.sample в .env и заполните необходимые данные
5. Создайте базу данных в PostgreSQL , которую указали в файле .env в параметре DATABASES_NAME
5. Выполните миграции, команда для Ubuntu

         python3 manage.py migrate

6. Создайте суперпользователя

         python3 manage.py csuser

7. Запустите Redis

         sudo service redis-server start
8. Запустите проект 

         python3 manage.py runserver
9. Перейдите в админку по адресу http://127.0.0.1:8000/admin. Введите параметры учетной записи admin@sky.pro и пароль 1238. 
Заполните пользователей с указанием ID телеграма и привычки.
10. В терминале Pycharm запустить службы worker и beat 

         celery -A config beat -l info -S django 
         python3 -m celery -A config worker -l info 
либо одной командой 

    пше celery -A config  worker --beat --scheduler django --loglevel=info
11. После этого каждую минуту (время можно изменить в параметре CELERY_BEAT_SCHEDULE файла SETTINGS) будет выполняться задача.




