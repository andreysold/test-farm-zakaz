# test-farm-zakaz

Развертывание проекта

1. git clone git@github.com:andreysold/test-farm-zakaz.git
2. cd test-farm-zakaz
3. python -m venv env
4. pip install -r farma/requirements.txt
5. настраиваес коннект к БД в Pycharm, переносим db.sqlite3 в Database => test connections => success
6. python manage.py farma/runserver 8000
