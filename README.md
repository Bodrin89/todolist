
# Планировщик задач
___

### стек

+ python3.10 <img height="24" width="24" src="https://cdn.simpleicons.org/python/5066b3" />
+ Django 4.1 <img height="24" width="24" src="https://cdn.simpleicons.org/django/5066b3" />
+ Postgres 15.0 <img height="24" width="24" src="https://cdn.simpleicons.org/postgresql/5066b3" />
+ Docker <img height="24" width="24" src="https://cdn.simpleicons.org/docker/5066b3" />
+ poetry<img height="24" width="24" src="https://cdn.simpleicons.org/poetry/" />
+ DRF 3.14
+ Pydentic 1.1
+ Docker-compose

В данном проекте реализован планировщик задач на Django с использованием DRF.
Список не обходимых переменных окружения находится в .env.dist



Ознакомиться с версией проекта можно по ссылке http://vbodrin.tk

## Установка:
1. Клонируйте репозиторий с github на локальный компьютер
2. Создайте виртуальное окружение
3. установите poetry командой `pip install poetry`
4. установите зависимости командой `poetry install`
5. Создайте в корне проекта файл в .env и заполните переменными окружения из .env.dist
6. Соберите и поднимите docker-контейнер командой `docker-compose up -d --build`


## Список приложений проекта и их реализация:
+ ### core
  + [x] Регистрация пользователя
  + [x] Login и Logout
  + [x] Обновление данных о пользователе и пароля
- ### goals
    + [x] Создание новой доски
    + [x] Получение списка досок пользователя
    + [x] Редактирование и удаление досок пользователя
    + [x] Создание новой категории
    + [x] Получение списка категорий где текущий user является участником
    + [x] Создание цели у категории
    + [x] Получение списка целей
    + [x] Редактирование и удаление целей
    + [x] Создание, редактирование и удаление комментариев у цели
- ### bot
    + [x] Реализованна аутентификация через telegram
    + [x] С помощью telegram-bot можно получить список целей
    + [x] С помощью telegram-bot можно создать новую цель

- ### SWAGGER: http://localhost:8000/docs/swagger

