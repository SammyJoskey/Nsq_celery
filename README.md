# Парсер вебсайтов
* Clone the repo
* From the repo dir:

1. Создаем БД:
* docker run --name postgres -e POSTGRES_PASSWORD=010101 -d -p 5432:5432 postgres
* docker exec -it postgres psql -U postgres
* create database parser;
2. Запускаем redis:
* docker run -d -p 6379:6379 redis
3. Запускаем flask
* flask run
4. Запускаем celery
* celery worker -A app.celery

Приложение запускается на  http://127.0.0.1:5000/ с двумя эндпоинтами:

/ — форма поиска слова «Python» по ссылке на вебсайт

/results — результаты подсчетов

