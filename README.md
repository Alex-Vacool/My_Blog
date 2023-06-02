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

## Установка веб-сервиса (Windows)
 - Для установки веб-сервиса необходимо скопировать содержимое репозитория на диск:
```curl   
git clone https://github.com/Alex-Vacool/My_Blog
```
 - Для работы сервиса необходимо поставить зависимости
```curl   
pip3 install -r requirements.txt
```
 - в папке my_blog/my_blog/settings.py создать файл .env c ключами:
```curl 
DJANGO_SECRET_KEY = 'django-insecure-f37d1kn&g8+^vhk*f6!0#9949a$*=*lo5y+u2k_bivwwk-$n=l'
token = 'ccb8c10a0f65187e910587fb1c6bac37ee6c4efc'
 ```

 - перейти в папку blog с файлом manage.py:
```curl 
cd my_blog
 ```

## Пример использования (Windows)
Чтобы протестировать веб-сервис необходимо:
 - запустить сервер:
```curl 
python manage.py runserver
```
 - перейти по адресу на сайт:
```curl 
http://127.0.0.1:8000/
```
зарегистрироваться и начать работу с блогом:
```curl 
меню "Регистрация"
```
