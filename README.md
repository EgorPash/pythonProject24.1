# Документация по проекту

## Запуск проекта с использованием Docker

1. Убедитесь, что у Вас установлен [Docker](https://www.docker.com/products/docker-desktop) и [Docker Compose](https://docs.docker.com/compose/).
   
2. Склонируйте этот репозиторий:

git clone <URL_вашего_репозитория>
cd <имя_папки_с_репозиторием>
3. Создайте файл `.env` с переменными окружения:

SECRET_KEY='your-secret-key'
DEBUG=True
DATABASE_NAME='your_database_name'
DATABASE_USER='postgres'
DATABASE_PASSWORD='your_password'
DATABASE_HOST='db'
DATABASE_PORT='5432'
STRIPE_TEST_SECRET_KEY='your-stripe-secret-key'
STRIPE_TEST_PUBLIC_KEY='your-stripe-public-key'

4. Постройте и запустите контейнеры:

docker-compose up --build


5. Получите доступ к приложению по адресу `http://localhost:8000`.

## Завершение работы

Чтобы остановить все контейнеры, используйте:

docker-compose down