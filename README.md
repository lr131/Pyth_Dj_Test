Проект управления базой студентов
===================


Это тестовый django-проект, который управляет базой студентов. 

----------


Что должно быть установлено
-------------

* Python 3
* Django 1.8.5
 
 Порядок действий при первом запуске
-------------
1. Для начала необходимо создать таблицы в базе данных. Сделать это можно при помощи  команды 
  `$ python manage.py migrate` 
или 
  `$ python manage.py syncdb`

2. Файл dbinitial_data.json переименовать в initial_data.json
3. Снова выполнить 
  `$ python manage.py migrate` 
или 
  `$ python manage.py syncdb`
4. Заупустить сервер 
  `$python manage.py runserver`

