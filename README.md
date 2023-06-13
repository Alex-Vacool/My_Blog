# Дипломный проект (Python)
## В качестве темы дипломного проекта предлагается WEB-сайт на Django, 6 страниц, для ведения блога неограниченным количеством пользователей, с возможностью создавать, модифицировать, удалять посты, назначением тэгов постам и т.п., регистрацией пользователей и возможностью администрирования через назначение прав.

Разворачивается на локальной машине Windows или Linux c использованием Docker.

#### Шаблон сайта взят с [https://startbootstrap.com/theme/clean-blog](https://startbootstrap.com/theme/clean-blog)
#### Диаграмма прецидентов системы представлена на рисунке
![Alt-текст](https://github.com/Alex-Vacool/Diploma/blob/58c1ddb248389168d099ede3d648f23237545349/%D0%94%D0%97_%D0%9F%D0%B8%D1%82%D0%BE%D0%BD.png)
## Оглавление

1. [Требования к операционной системе](#Требования-к-операционной-системе)
2. [Установка веб-сервиса Windows](#Установка-веб-сервиса-Windows)
3. [Пример использования Windows](#Пример-использования-Windows)

## Требования к операционной системе
Тестирование сервиса проводилось на операционной системе Windows 11 c python 3.7</sup>

## Установка веб-сервиса Windows
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

## Пример использования Windows
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
## Установка веб-сервиса (Linux)
 - Подключиться по ssh (putty, ssh)
 - Перекинуть файлы проекта (ftp, git)
 - Настроить службу ftp на сервере: 
 ```curl 
sudo apt update
 ```
 ```curl 
sudo apt install vsftpd
 ```
 ```curl 
service vsftpd status
 ```
 - Включить возможность записи по ftp
 - Установить nano 
 ```curl 
sudo apt install nano
 ```
 - Отредактировать файл с настройками
 ```curl 
nano /etc/vsftpd.conf
 ```
  ```curl 
write_enable=YES
Chtl+O - сохранить
Ctrl+X - закрыть
 ```
 - Подключиться с помощью WinSCP
 - Скоптровать файлы в каталог /home/ubuntu - (пример для Ubuntu Server)
 - Даем права 755 (Чтение и выполнение)
 - Создать python-окружение для проекта
 ```curl 
python3 -V - текущая версия
 ```
 ```curl 
sudo apt install python3-venv
 ```
 ```curl 
python3 -m venv django2
 ```
 ```curl 
source django2/bin/activate
 ```
 - Установить необходимые пакеты в окружение
 ```curl 
pip install -r requirements.txt
 ```
 - Установить gunicorn (uwsgi) в текущее окружение
 ```curl 
pip install gunicorn
 ```
 - Провести тестовый запуск проекта (из папки проекта)
 ```curl 
gunicorn my_blog.wsgi 
 ```
- Зарегистрировать gunicorn как сервис (сеть, сокет)
 ```curl 
sudo nano /etc/systemd/system/gunicorn.service
 ```
- Текст файла
 ```curl 
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/home/ubuntu/my_blog
ExecStart=/home/ubuntu/my_blog/django2/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/my_blog/my_blog.sock my_blog.wsgi

[Install]
WantedBy=multi-user.target
 ```
- Регистрация и запуск сервиса
```curl 
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
service gunicorn status - должен быть active
 ```
- Установить nginx
```curl 
sudo apt install nginx
service nginx status
 ```
 - Настроить nginx
 ```curl 
cd /etc/nginx/sites-available/
 ```
 - Перенаправить запросы на сокет gunicorn
 ```curl 
nano default

текст фала

server {
    listen 80;
    server_name 192.168.0.98;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/my_blog;
    }

    location /media/ {
        root /home/ubuntu/my_blog;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/my_blog/my_blog.sock;
    }
}
 ```
 - Перезапустить сервисы gunicorn и nginx 
```curl 
service gunicorn restart
service nginx restart
 ```





