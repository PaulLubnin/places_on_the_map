# Яндекс.Афиша
Сайт - карта, на которой можно найти места для интересного времяпрепровождения.

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
Затем из папки с проектом в командной строке наберите и установите необходимые зависимости:
```
pip install -r requirements.txt
```

Создайте `.env` файл, в нем определите переменные:
```
DEBUG=True
DJANGO_SECRET_KEY=long string
ALLOWED_HOSTS=localhost, 127.0.0.1
```

## Как запустить:
```
python manage.py migrate
```

```
python manage.py runserver
```

### Данные:
```
python manage.py load_places -url https://github.com/devmanorg/where-to-go-places/tree/master/places
```

### Администрирование:
```
python manage.py createsuperuser
```