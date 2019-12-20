run:
	./manage.py runserver

test:
	./manage.py test --keepdb

pep8:
	flake8
