# CarWallet
API для учёта расходов на свои транспортные средства.

## Используемый стэк
1. FastAPI
2. PostgreSQL, SQLAlchemy
3. Alembic, pydantic

## Как запустить проект
> Для работоспособности проекта у вас должен быть установлен Postgres и создана БД с параметрами которые вы укажите в ".env"
1. Укажите в FastAPI_APP/env-template.env свои данные вместо user, pwd, host, port, db_name, либо создайте свой ".env" и заполните данные по примеру из ".env-template"
2. Установите зависимости
```
pip install -r requirements.txt
```
3. Перейдите в директорию FastAPI_app примените миграции
```
alembic upgrade head
```
4. Оставаясь в директории FastAPI_app, выполните команду
```
python3 main.py
```
5. После запуска проект доступен по ссылке http://localhost:8080/docs
