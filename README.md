# KYC_admin
<b>Панель Django Admin</b>
<h3>Подготовка к запуску:</h3>

1. Клонируйте репозиторий;</br>
2. Создайте в корневой директории проекта и заполните файл .env:</br>

```
SECRET_KEY='<Секретный ключ>'

POSTGRES_DB='<Имя базы данных>'
POSTGRES_USER='<Логин>'
POSTGRES_PASSWORD='<Пароль>'
POSTGRES_HOST='localhost'
POSTGRES_PORT='5432'

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=587
EMAIL_USER='<имя пользователя (почта)>'
EMAIL_PASSWORD='<пароль>'
EMAIL_USE_TLS=True

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

</br>
<h3>Создание и применение миграций</h3>
</br>
При парной работе с KYC_api, миграции выполнять в данном проекте!

```bash
python3 manage.py makemigrations 
```
```bash
python3 manage.py mifrate
```
<h3>Создание суперпользователя</h3>

```bash
python3 manage.py ccsu
```

<h3>Запуск</h3>

```bash
python manage.py runserver 0.0.0.0:8001
```