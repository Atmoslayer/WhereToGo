# Куда пойти
Проект представляет карту Москвы с отмеченными на ней местами, интересными для посещения. По нажатию 
на интересующее место можно получить дополнительную информацию по нему.
## Тестовая версия сайта
У проекта существует [тестовая версия сайта](http://atmoslayer.pythonanywhere.com/), размещённая с помощью сервиса 
[pythonanywhere.com](https://www.pythonanywhere.com). 
## Как установить
### Переменные окружения 
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.
Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
### Запуск проекта
- Python3 должен быть уже установлен. 
- Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей: `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`
## Наполенение данными
Помимо добавления данных через админ-панель можно воспользоваться командой `python3 manage.py load_place`.
Команда позволяет загружать в БД данные из json файлов, ссылки на которые нужно указать при запуске.
### Пример json файла
json файлы должны иметь следующий вид:
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
В указанном файле содержится название достопремичательности, её короткое и длинное описание, координаты 
и ссылки на картинки.
### Указание ссылок на json файлы
Для указания собственных путей используйте аргумент  `-urls`: `python manage.py load_place -urls https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/Арт-пространство%20«Бункер%20703».json`.
`-urls` поддерживает любое количества ссылок, для последовательного скачивания нескольких файлов 
достаточно просто передать ссылки на них друг за другом без разделителей.
После запуска скрипта данные из файла будут сохраняться в базу данных. Т.к. процесс может занять много времени, его 
ход отображается в консоли. 
Для тестовой версии проекта данные были взяты из [репозитория](https://github.com/devmanorg/where-to-go-places).
В случае с гитхабом для получения ссылки на json файл откройте его с помощью кнопки `Raw`. После этого будет 
получен путь к файлу, который можно скопировать из адресной строки.
## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).