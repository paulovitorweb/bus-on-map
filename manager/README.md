# Manager

An application to manage public transport data such as routes.

## Requirements
 - Python >= 3.8.10
 - PostgreSQL with PostGIS extension

## Development

To run application for development, first run

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

This application use GeoDjango, and some geospatial dependencies are required. Please, see [GeoDjango instalation](https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/).

Create an `.env` file with the following content in the root folder:

```
SECRET_KEY=<django-secret-key>
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@admin.com
```

Create a superuser with

```
make create-su
```

And run database migrations

```
python manage.py migrate
```

Finally, run server

```
python manage.py runserver
```