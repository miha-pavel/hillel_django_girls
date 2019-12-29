# hillel_django_girls
Studying djangogirls tutorial
This project supposed to run on `python3`


## Location
This site locate [GitHub Pages](https://github.com/miha-pavel/hillel_django_girls)


## Before first launch
```
1. python3 -m venv env
2. . env/bin/activate
3. pip install -r requirements.txt
4. Configure project using `local_setings.dev.py` as example. Your local settings should be written in `local_setings.py`
5. python manage.py migrate
```


## Run Django project
```
python manage.py runserver
```
Or use makefile guide


## Makefile guide
* ```make run``` - will run Django developer server at 8000 port
* ```make test``` - will test the project with --keepdb option
* ```make pep8``` - will check the code with pylint.
* ```make sh_p``` - will open shell_plus IDEA in the terminal.
* ```make migrate``` - will make "python manage.py migrate".