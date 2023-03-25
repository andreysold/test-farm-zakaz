# test-farm-zakaz

Развертывание проекта

1. git clone git@github.com:andreysold/test-farm-zakaz.git
2. cd test-farm-zakaz
3. python (python3) -m venv env
4. source env/bin/activate
5. pip install -r farma/requirements.txt
6. cd farma
7. docker compose up
8. python manage.py makemigrations
9. python manage.py migrate
10. python manage.py runserver 8000
