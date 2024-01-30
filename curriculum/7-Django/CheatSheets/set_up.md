# Building a Simple Django API with Django and Django REST Framework

In this markdown file, we will guide you through the process of building a simple Django API using Django and Django REST Framework. We will cover the essential steps required to set up the project, define models, serializers, views, and URLs.

## Step 0: Installments

1. Create and activate a Python Virtual Environment

```bash
python -m venv <name_of_env>
source <name_of_env>/bin/activate
```

2. Install all necessary packages

```bash
pip install django #installs django
pip install "psycopg[binary]" #installs psycopg3 which allows django to talk to postgresql
pip install djangorestframework #install rest_framework to allow us to utilize Response, APIView, and TokenAuthentication
pip install django-cors-headers #installs corsheaders
```

3. Create DB in PostgreSQL

```bash
# in terminal
createdb <name_of_db>
# in postgres
CREATE DATABASE <name_of_db>;
```

## Step 1: Set up a Django Project

1. Create a new Django project using the following command:

```bash
django-admin startproject myapi . #<=== DON'T FORGET THE PERIOD
```

2. Connect your PostgreSQL database under `myapi/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', #<== Points to PostgreSQL
        'NAME': '<name_of_db>', #<=== Points to the correct Database
    }
}
```

## Step 2: Create a Django App

1. Create a new Django app within your project using the following command:

```bash
python manage.py startapp myapp
```

2. Register the app in the project's `settings.py` file by adding `'myapp'` to the `INSTALLED_APPS` list, and add `'rest_framework'` to the `INSTALLED_APPS` list.

## Step 3: Define Models

1. Open the `myapp/models.py` file and define your models using Django's model fields.

2. Add validators onto your models from `django.core import validators as v`

3. Run migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Test your models

## Step 5: Define Views

1. Open the `myapp/views.py` file and define views based on the desired API endpoints.

2. Views handle HTTP requests and return responses.

## Step 6: Configure URLs

1. Connect `myapi/urls.py` to `myapp/urls.py` utilizing `include("myapp.urls")`
2. Create and open the `myapi/urls.py` file and add the URL patterns for your API.
3. Connect the API endpoints to the corresponding views defined in `myapp/views.py`.

## Step 7: Test the API

1. Start the development server:

```bash
python manage.py runserver
```

2. Open a web browser and navigate to `http://localhost:8000/` to access the API root.

3. Interact with the API by making HTTP requests to the defined endpoints.

## Conclusion

By following these steps, you can create a simple Django API using Django and Django REST Framework. Remember to define models, serializers, views, and URLs to handle various API operations. This is just the beginning, and you can further enhance your API by adding authentication, permissions, and additional features based on your project requirements.
