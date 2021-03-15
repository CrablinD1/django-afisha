# Неяндекс.Афиша.

Проект доступен по ссылке: http://crablin.pythonanywhere.com

Панель администратора: http://crablin.pythonanywhere.com/admin

Карта Москвы с интересными местами.

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.

### Инструкция по локальному запуску (для разработчика)   
1. Скачать репозиторий: 
   ```
   git clone https://github.com/CrablinD1/django-afisha.git
   ```
2. Перейти в папку проекта:
   ```
   cd where_to_go
   ```
3. Создайте файл переменных .env для settings.py в каталоге where_to_go:
   ```
   SECRET_KEY = "your_key"
   DEBUG = True
   ```
4. Создать и активировать виртуальное окружение удобным для вас способом:
   ```
   python3 -m venv <your-venv-name>
   source <your-venv-name>/bin/activate
   ```
5. Установить зависимости:
   ```
   pip install -r requirements.txt
   ```
6. Запустить миграции:
    ```
   python manage.py migrate
   ```
7. Запустить сервер:
    ```
   python manage.py runserver
   ```
8. Сайт запущен на локалхосте по адресу http://127.0.0.1:8000. Теперь можно создать суперюзера:
    ```
   python manage.py createsuperuser
   ```
9. Пока на сайте нет локаций. Чтобы поместить локацию на карту, запустите скрипт cо ссылкой на файл локации:
    ```
   python manage.py load_place <link>  
   ```
   Примеры команд для загрузки данных в файле places.txt
   
