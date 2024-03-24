dependencies:
	pip install -r requirements.txt

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

runserver:
	python3 manage.py runserver

runserver-devices:
	python3 manage.py runserver 0.0.0.0:8000

populate-db:
	python3 manage.py $(M)
