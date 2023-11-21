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
- установите необходимые зависимости:

    - на боевом сервере:
    ```
    pip install -r requirements.txt
    ```
  
    - на локальной машине:
    ```
    pip install -r dev-requirements.txt
    ```
---

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, 
создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком 
формате: `ПЕРЕМЕННАЯ=значение`.

Доступные переменные:
- `DEBUG` — режим отладки. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта, он используется для обеспечения криптографической подписи и должен иметь уникальное, непредсказуемое значение.
- `ALLOWED_HOSTS` — смотри [документацию Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).

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
- заполнените БД данными:
  
  - весь список локаций:
  ```
  python manage.py load_places -url https://github.com/devmanorg/where-to-go-places/tree/master/places
  ```
  - по одной локации из json:
  ```
  python manage.py load_places -json [ссылка на json]
  ```  
  пример json'a:
  ```
  {
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
  }
  ```

- на боевом сервере подключите статику:
```
python manage.py collectstatic
```
---
### Администрирование
- для доступа к админке сайта необходимо создать администратора:
```
python manage.py createsuperuser
```

---
Запущенный пример проекта можно посмотреть [тут](https://paulego.pythonanywhere.com/)