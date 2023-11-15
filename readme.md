# Интересные места Москвы.
Сайт - карта, на которой можно найти места для интересного времяпрепровождения.

---
## Как установить
Для установки необходим [Python>=3.8](https://www.python.org/downloads/) и [git](https://git-scm.com/downloads).
После установки Python и Git можно приступать к разворачиванию проекта.

Склонируйте проект:
```
https://github.com/PaulLubnin/places_on_the_map.git
```
В папке с проектом создайте отдельную среду для установки всех зависимостей, затем активируйте её:

- если у вас установлен только один Python:
```
python -m venv env
```
- если у вас установлены несколько разных версии Python:
```
py -3.8 -m venv env
```
- активируйте виртуальную среду:
```
env\Scripts\activate
```
- затем из папки с проектом в командной строке наберите и установите необходимые зависимости:
```
pip install -r requirements.txt
```

Создайте `.env` файл, в нем определите переменные:
```
DEBUG=True
DJANGO_SECRET_KEY=long string
ALLOWED_HOSTS=localhost,127.0.0.1
```
---
## Как запустить
- создайте базу данных
```
python manage.py migrate
```
- запустите сервер
```
python manage.py runserver
```
- заполнените БД данными, воспользовавшись командой:
```
python manage.py load_places -url https://github.com/devmanorg/where-to-go-places/tree/master/places
```
---
### Администрирование
- для доступа к админке сайта необходимо создать администратора:
```
python manage.py createsuperuser
```

---
Запущенный пример проекта можно посмотреть [тут](https://paulego.pythonanywhere.com/)