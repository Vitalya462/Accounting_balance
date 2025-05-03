MANAGE_FILE_PATH=backend/manage.py



run:
	python $(MANAGE_FILE_PATH) runserver

makemigrations:
	python $(MANAGE_FILE_PATH) makemigrations

migrate:
	python $(MANAGE_FILE_PATH) migrate

mksu:
	python $(MANAGE_FILE_PATH) createsuperuser
