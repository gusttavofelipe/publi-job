.env: local.env
	@cp -n local.env .env || echo "NOTE: review your .env file comparing with local.env"
	@touch .env

setup-dev: .env
	@pip install -r > requirements.txt

pyenv:
	@pyenv virtualenv 3.11.0 publi
	@pyenv activate publi

migrate-db:
	@python manage.py makemigrations
	@python manage.py migrate