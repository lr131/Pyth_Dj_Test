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

2. Загрузить данные 
  `$ python manage.py loaddata initial_data`
3. Заупустить сервер 
  `$python manage.py runserver`

-------------
without workon:

user@linux-03t9:~> cd ~/environments/

source test/bin/activate
