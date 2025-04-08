MANAGE_FILE_PATH=manage.py


run:
	sudo systemctl start minio
	python $(MANAGE_FILE_PATH) runserver

makemigrations:
	python $(MANAGE_FILE_PATH) makemigrations

migrate:
	python $(MANAGE_FILE_PATH) migrate

mksu:
	python $(MANAGE_FILE_PATH) createsuperuser