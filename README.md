# django-drf-boilerplate
Boilerplate project using Django and Django REST Framework.
Currently supporting only Python 3.x.

**IMPORTANT**:
Make sure you have Django 2.0 installed on your environment.

## Download Project Template
```bash
$ django-admin.py startproject --template=https://github.com/sbtur/django-drf-boilerplate/archive/master.zip <project_name> .

 ```

## Postgre SQL
Install Postgres and Start service on your Operating System;
Login Postgres psql -U postgres;

Create the DB CREATE DATABASE db_name;

## Postgre SQL with Docker
Creating local DB:
Initialize docker docker-compose up;
	- Run docker ps;
	- Access DB docker instance docker exec -it docker-hash bash;
	- Access Postgres psql -U postgres;
	- Create the DB CREATE DATABASE db_name;


## How to configure database URL
Copy file src/app/ex.env to src/app/.env
Set URL database in the file src/app/.env

## How to install app
```bash
$ cd [project_name]
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pip install -r requirements_test.txt
$ python src/manage.py migrate
$ python src/manage.py createsuperuser
$ python src/manage.py runserver
```

## How to test app
```bash
$ cd [project_name]
$ pytest -s
```

## Generate token validate API - Django Admin
http://localhost:8000/admin/
AUTH TOKEN -> Add Token

## Install git pre-commit hook
Check code syntax and style before commit changes.

After initializing git, add flake8 hook.
```bash
$ python -m flake8 --install-hook git
$ pre-commit install
```

Set flake8 strict parameter to true, this forces all violations to be fixed
before the commit.
```bash
$ git config --bool flake8.strict true


