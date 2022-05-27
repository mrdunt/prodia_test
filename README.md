# prodia_test
Prodia Test, Check current weather


# How to run this project

1. Create virtualenv on local and activate it
2. Setup db for projects (this project using postgre)
3. install requirements into your virtual env with ```pip install -r requirements.txt```
4. create file named ```settings_local.py``` for storing credentials environment
5. Fill your ```settings_local.py``` with your credentials db, url api, apikey
6. Migrate this project to your db with ```python manage.py migrate```
7. Create superuser for login with ```python manage.py createsuperuser``` and follow the instructions until done
8. Ta-da ! You can start this project with ```python manage.py runserver```

If something went wrong, don't hesitate email me danan.nr@gmail.com .
