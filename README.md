# rs-back

Бэкенд сайта «Центра молодёжной робототехники»

## Необходимо

Пакетный менеджер Python - [Poetry](https://python-poetry.org/).

## Как запускать?

1. Склонировать репозиторий и перейти в рабочую директорию.

```shell
git clone git@github.com:bmstu-itstech/rs-back.git
cd fivvt-backend
```

2. Создать виртуальное окружение Python (venv) через Poetry.
```shell
poetry env use python3
```

3. Установить зависимости через Poetry.
```shell
poetry install --no-root 
```

4. Создать базу данных, применить существующие миграции.
```shell
python3 manage.py migrate 
```

5. Создать супер-пользователя для страницы администратора.
```shell
python3 manage.py createsuperuser
```

5. Запустить сервер. По умолчанию будет запущен на http://localhost:8000/
```shell
python3 manage.py runserver 
```

## Полезные страницы

- Страница администратора: http://localhost:8000/admin
- Документация в Swagger: http://localhost:8000/api/swagger
