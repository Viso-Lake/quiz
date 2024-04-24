PM = python ./backend/manage.py

run:
	$(PM) runserver  8010

mg:
	$(PM) makemigrations
	$(PM) migrate

superu:
	$(PM) createsuperuser

freeze:
	pip freeze > reqirements.txt
