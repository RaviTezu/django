django
======
For Learning Django


Commands: 
===
| For?                                 | Command                                      |
|--------------------------------------|----------------------------------------------|
| To start a Project:                  | django-admin.py startproject  [project-name] |
| To start a Application:              | django-admin.py startapp [app-name]          |
| To create Tables from models:        | python manage.py syncdb                      |
| To start django dev server:          | python manange.py runserver                  |
| To launch Python shell:              | python manage.py shell                       |
| To list all available commands:      | python manage.py list                        |
| To see all SQL that Django executes: | python manage.py sql [app-name]              |
| To get more help:                    | python manage.py sql --help                  |

Admin site:
===
- http://127.0.0.1:8000/admin when using django development server
- You may need to enale this app in settings.py and urls.py
- For creating a super user: python manage.py createsuperuser --username=admin --email=admin@example.com
