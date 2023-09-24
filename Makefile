.env: local.env
	@cp -n local.env .env || echo "NOTE: review your .env file comparing with local.env"
	@touch .env

setup-dev: .env
	@pip install -r > requirements.txt 