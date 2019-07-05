# django-drf-boilerplate
Boilerplate project using Django and Django REST Framework.
Currently supporting only Python 3.x.

**IMPORTANT**:
Make sure you have Django 2.0 installed on your environment.
Docker Compose is used *just* for development environment. The Dockerfile works without it.

## Download Project Template
```bash
$ django-admin.py startproject \
  --template=https://github.com/sbtur/django-drf-boilerplate/archive/master.zip \
  <project_name> .

 ```

## How to configure database URL
Copy file src/app/ex.env to src/app/.env
Set URL data base in the file src/app/.env
Set new database name in the file docker-compose.yml [POSTGRES_DB: django-drf-bloilerplate]

## How to install without Docker

```bash
$ pip install -r requirements.txt
$ python src/manage.py migrate
$ python src/manage.py createsuperuser
$ python src/manage.py runserver

```

## How to install with Docker Compose

```bash
$ docker-compose up
$ docker ps [get name container not image]
$ docker exec -i -t django-drf-boilerplate_web_1 /bin/bash
$ python src/manage.py createsuperuser
$ exit
```

## Django Admin
http://localhost:8000/admin/


## Install git pre-commit hook
Check code syntax and style before commit changes.

After initializing git, add flake8 hook.
```bash
$ git init
$ python -m flake8 --install-hook git
```

Set flake8 strict parameter to true, this forces all violations to be fixed
before the commit.
```bash
$ git config --bool flake8.strict true
```

## Database with Docker
Running database on latest PostgreSQL Docker container running in the port `5432`. The connection is defined by the `dj-database-url` package. There's a race condition script to avoid running Django before the database goes up.

<!--- ## Docs -->
<!--- Let's face it, human memory sucks. Will you remember every detail that involves your project 6 months from now? How about when the pressure is on? A project with good documentation that explains all the facets, interactions and architectural choices means you and your teammates won't have to spend hours trying to figure it out later. You can find a template to get started [here](https://github.com/sbtur/django-drf-boilerplate/wiki/Docs-Template). -->
