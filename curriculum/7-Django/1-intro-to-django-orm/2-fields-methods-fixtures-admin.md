# Expanding on Django and Django ORM

## Intro

Earlier we created a `Pokemon` model, but we only touched the tip of the iceberg when it comes to model fields. Lets take it a step further and take a look at some useful fields and features.

- [SLIDES](https://docs.google.com/presentation/d/1o4ntpnNJWVLU4aim7cFFPAV4wzZf2bSr88CBKlLUxcQ/edit?usp=drive_link)

## Useful Model Fields

```python
# utilize timezone for any Django Date/DateTime/TZ fields since it already provides
# the correct format

# DateField will accept a date in the following format "YYYY-MM-DD"
date_of_birth = models.DateField()

#DateTimeField will accept a data, time, and timezone in the following format "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format."
last_time_at_school = models.DateTimeField()

# DecimalField will take in decimal numbers and you can specify how many decimal places
# are allowed and/or how many overall digits are allowed.
daily_allowance = models.DecimalField(decimal_places = 2)

# IntegerField will take in whole numbers only but does not care if integer holds a positive or negatice value if you want only positive integers utilize PositiveIntegerField
year_of_schooling = models.IntegerField()


# TextField, unlike CharField TextField does not have any maximum character count.
description = models.TextField()

# BooleanField will take in boolean values only
good_pokmon = models.BooleanField()

```

> When defining a model field, you have the ability to set the null=True and the blank=True options. By default, they are False. Knowing when to use these options is a common source of confusion for developers.

| Field Type                                                                                        | Setting null=True                                                                                                                                                                         | Setting blank=True                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CharField,<br>TextField,<br>SlugField,<br>EmailField,<br>CommaSeparatedIntegerField,<br>UUIDField | Okay if you also have set both unique=True and blank=True. In this situation, null=True is required to avoid unique constraint violations when saving multiple objects with blank values. | Okay if you want the corresponding form widget to accept empty values. If you set this, empty values are stored as NULL in the database if null=True and unique=True are also set. Otherwise, they get stored as empty strings. |
| FileField,<br>ImageField                                                                          | Don’t do this.<br>Django stores the path from MEDIA_ROOT to the file or to the image in a CharField, so the same pattern applies to FileFields.                                           | Okay.<br>The same pattern for CharField applies here.                                                                                                                                                                           |
| BooleanField                                                                                      | Okay.                                                                                                                                                                                     | Default is blank=True.                                                                                                                                                                                                          |
| IntegerField,<br>FloatField,<br>DecimalField,<br>DurationField, etc.                              | Okay if you want to be able to set the value to NULL in the database.                                                                                                                     | Okay if you want the corresponding form widget to accept empty values. If so, you will also want to set null=True.                                                                                                              |
| DateTimeField,<br>DateField,<br>TimeField, etc.                                                   | Okay if you want to be able to set the value to NULL in the database.                                                                                                                     | Okay if you want the corresponding form widget to accept empty values, or if you are using auto_now or auto_now_add. If it’s the former, you will also want to set null=True.                                                   |
| ForeignKey,<br>OneToOneField                                                                      | Okay if you want to be able to set the value to NULL in the database.                                                                                                                     | Okay if you want the corresponding form widget (e.g. the select box) to accept empty values. If so, you will also want to set null=True.                                                                                        |
| ManyToManyField                                                                                   | Null has no effect                                                                                                                                                                        | Okay if you want the corresponding form widget (e.g. the select box) to accept empty values.                                                                                                                                    |
| GenericIPAddressField                                                                             | Okay if you want to be able to set the value to NULL in the database.                                                                                                                     | Okay if you want to make the corresponding field widget accept empty values. If so, you will also want to set null=True.                                                                                                        |
| JSONField                                                                                         | Okay.                                                                                                                                                                                     | Okay.                                                                                                                                                                                                                           |

## Improving our Pokemon Model

> We may be tempted to add new fields to our model and or change default or standard values to then enter our Django Python Shell to create a couple of new instances. Although it's tempting, it's important to backup any existing data before making any sort of model changes to our Django Models. Our updated Models could cause some unexpected behavior with already existing data and we would have to manually fix it ourselves if we don't properly backup our data. This is where fixtures comes in handy.

### **Fixtures**

> Create a `fixtures` directory inside of our 'pokemon_app' and make a file named `pokemon_data.json` within it.

```bash
    mkdir pokemon_app/fixtures
    # the following command will dump our PostgresSQL data from this data table onto a json 
    # file named pokemon_data.json. Notice we haven't created said file just yet so it's sage 
    # to assume that Django will generate this json file for us.
    python manage.py dumpdata pokemon_app.Pokemon --indent 2 > pokemon_app/fixtures/pokemon_data.json
```

- You'll see that dumpdata created a new json file inside the fixtures directory

```json
    // Will display each Pokemon Instance in json format
[
    {
        "model": "pokemon_app.pokemon",
        "pk": 1,
        "fields": {
            "name": "Pikachu",
            "level": 12
        }
    }
]
```

> Just like Django allows to "back up" your data by dumping it onto a JSON file. Django also allows you to load data from a JSON file through the `loaddata` command.

```bash
    python manage.py loaddata pokemon_data.json
    Installed 1 object(s) from 1 fixture(s)
```

### Updating the Pokemon Model

Lets apply some of new fields to our Pokemon model and provide some default values.

```python
from django.db import models
from django.utils import timezone

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    # IntegerField will allow only solid numerical values as input
    level = models.IntegerField(default=1)
    # We are providing a default to someone born Jan 1st 2008
    date_encountered = models.DateField(default="2008-01-01")
    # If a value is not provided we are stating the last time this pokemon was at school was upon creation of the classes instance.
    date_captured = models.DateTimeField(default=timezone.now)
    # If no value is provided the Pokemon description will be "Unknown"
    description = models.TextField(default="Unknown")
    # We must catch them all.
    captured = models.BooleanField(default = False)
```

> Now that our existing data has been "backed up", we can apply these new fields onto our Data Base Pokemon Table.

```bash
    # Migrate our updated Pokemon Model
    python manage.py makemigrations
    python manage.py migrate
```

> Our new fields have been added onto our Pokemon Data Table on PostgreSQL. Let's enter the `Django Python Shell` and create a new Pokemon named Charizard.

```python
    # Enter Django Python Shell and Create new Pokemon
    python manage.py shell
    >>> from pokemon_app.models import Pokemon
    >>> charizard = Pokemon(name = 'Charizard', level = 25, date_encountered = "2007-04-07", captured = True)
    >>> charizard.save()

    # If I print charizard now I'll see a Pokemon object with the number 2 representing the second entry to this Data Table. 
    >>> print(charizard)
    Pokemon object (2) #<== This isn't really useful but don't worry we will address this shortly
    >>> exit()
```

## Adding class methods to our Models

We just saw that printing an instance returns a `Pokemon object (#)`, but we want to be able to actually see our Pokemon details. Django Models are still at its root just Python Classes, which means we can give these models class and instance methods that we can utilize through out our Django Application.

```python
    # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self):
        self.level += 1
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self):
        self.captured = not self.captured
        self.save()
```

> We do not need to `makemigrations` for class methods, so lets go back into our Django Python Shell and test out these methods.

```python
    # TERMINAL
    python manage.py shell
    >>> from pokemon_app.models import Pokemon
    >>> pokemon = Pokemon.objects.all()
    >>> print(pokemon)
    # Now we see Pikachu and Charizard's dunder methods
    <QuerySet [<Pokemon: Pikachu is yet to be caught>, <Pokemon: Charizard has been captured>]>
    # lets update Pikachus caught status and watch their dunder method change.
    >>> pokemon[0].change_caught_status()
    >>> print(pokemon)
    # You can see the value of the dunder method has changed
    <QuerySet [<Pokemon: Charizard has been captured>, <Pokemon: Pikachu has been captured>]>
    # Lets add one final Pokemon through our shell and move on to the Django Admin Site
    >>> blastoise = Pokemon(name = 'Blastoise', level = 37)
    >>> blastoise.save()
    >>> exit()
```

## Django Admin Site

> When people ask, “What are the benefits of Django over other web frameworks?” the admin is what usually comes to mind.
> Imagine if every gallon of ice cream (aka a Djanog Model) came with an admin interface. You’d be able to not just see the list of ingredients, but also add/edit/delete ingredients. If someone was messing around with your ice cream in a way that you didn’t like, you could limit or revoke their access.
> So far we've utilized the Django Shell to interact with our models, and although it works, it could definitely be more useful to have a more interactive site and that's where the Django admin site comes in.

> First lets register our `Pokemon Model` onto Django Admins Site.

```python
    # Pokemon_app/admin.py
    from django.contrib import admin
    # Explecit import of Pokemon Model
    from .models import Pokemon

    # Register your models here.
    admin.site.register([Pokemon])
```

> Now before entering our Admin Site with Django we must create a super user to log into our admin site and manipulate our models. Well what is a super user? Just like your local computer has a super user, every Django Application can also have one or more super users to conduct different administrative actions within our application.

```bash
    python manage.py createsuperuser
    # You'll be prompted to provide a username, email, and password
```

> Finally we are ready to enter our Admin Site and interact with our `Pokemon Model`. To do this we will have to run the Django server to host our Django application on our localhost. WE ARE NOT COVERING THE DJANGO SERVER OR HOW IT WORKS JUST YET. For now, please concentrate on the amazing feature the Django Admin Site has to offer.

```bash
    python manage.py runserver
```

> Once your server is running, open up your browser and go to [http:localhost:8000/admin](http:localhost:8000/admin), log in and you'll have a well constructed user interface to interact with your models. Press `ctrl + C` to kill your server and free your terminal.
