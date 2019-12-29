run:
	./manage.py runserver

test:
	./manage.py test --keepdb

pep8:
	flake8

sh_p:
	./manage.py shell_plus

migrate:
	python manage.py migrate
