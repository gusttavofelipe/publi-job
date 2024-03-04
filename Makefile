dependencies:
	pip install -r requirements.txt

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

runserver:
	python manage.py runserver 0.0.0.0:8000
