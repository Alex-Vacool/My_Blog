# Дипломный проект (Python)
## В качестве темы дипломного проекта предлагается WEB-сайт на Django, 6 страниц, для ведения блога неограниченным количеством пользователей, с возможностью создавать, модифицировать, удалять посты, назначением тэгов постам и т.п., регистрацией пользователей и возможностью администрирования через назначение прав.

Разворачивается на локальной машине Windows или Linux c использованием Docker.

#### Шаблон сайта взят с [https://startbootstrap.com/theme/clean-blog](https://startbootstrap.com/theme/clean-blog)
#### Диаграмма прецидентов системы представлена на рисунке
![Alt-текст](https://github.com/Alex-Vacool/Nginx-Docker/blob/main/%D0%94%D0%97_%D0%9F%D0%B8%D1%82%D0%BE%D0%BD.png)
## Оглавление

1. [Требования к операционной системе](#Требования-к-операционной-системе)
2. [Установка веб-сервиса](#Установка-веб-сервиса)
3. [Пример использования](#Пример-использования)

## Требования к операционной системе
Тестирование сервиса проводилось на операционной системе Windows 11 c python 3.7</sup>

## Установка веб-сервиса
 - Для установки веб-сервиса необходимо скопировать содержимое репозитория на диск:
```curl   
git clone https://github.com/Alex-Vacool/My_Blog
```
 - Для работы сервиса необходимо поставить зависимости
```curl   
pip3 install -r requirements.txt
```
 - в папке my_blog/my_blog/settings.py создать файл .env c ключом:
```curl 
DJANGO_SECRET_KEY = 'django-insecure-f37d1kn&g8+^vhk*f6!0#9949a$*=*lo5y+u2k_bivwwk-$n=l'
token = 'ccb8c10a0f65187e910587fb1c6bac37ee6c4efc'
 ```

 - перейти в папку blog с файлом manage.py:
```curl 
cd my_blog
 ```

 - сбросить все миграции:
```curl 
python manage.py migrate blogapp zero --fake
```
 - удалить файлы миграции в каталоге migrations:
```curl 
0001_initial.py и др. 000...
```
 - создать файлы миграции командой:
```curl 
python manage.py makemigrations
```
 - сделать миграции в базу командой:
```curl 
python manage.py migrate
```
 - создать суперпользователя:
```curl 
python manage.py createsuperuser
```
## Пример использования
Чтобы протестировать веб-сервис необходимо:
 - загрузить данные в базу:
```curl 
python manage.py fill_goods
```
 - запустить сервер:
```curl 
python manage.py runserver
```
 - перейти по адресу и посмотреть данные Merchandise через админку:
```curl 
http://127.0.0.1:8000/admin/
```

если порт забился:
```curl 
sudo fuser -k 8000/tcp
```


если порт забился:
```curl 
sudo fuser -k 8000/tcp
```
Можно собрать статистику по товарам и пользователям через API:
```curl 
http://127.0.0.1:8000/api/
```
автоматически рисовать диаграмму отношений классов модели:
```curl 
python manage.py graph_models -a -o models.png
```
https://russianblogs.com/article/80721384625/







