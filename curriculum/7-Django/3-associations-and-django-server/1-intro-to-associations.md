# Django Associations

## Intro

So far we've created a pokemon model in our pokemon_app for every pokemon in a Pokedex. Now we need to create a `Moves` model for pokemon to create associations between pokemon moves and pokemon. Just like in OOP we want to try and keep the `single responsibility principle` with our apps, meaning that each app should do only ONE thing and do it WELL.

- [SLIDES](https://docs.google.com/presentation/d/1mYcKl9VxQuqyfC7YM6W7mzopsMYU5ZAl6X6xoRFOU2Y/edit?usp=drive_link)

## Creating our Moves App and Model

> Let's quickly create a `move_app` and `Move` model to interact with our pokemon.

```bash
  # TERMINAL
  python manage.py startapp move_app
```

> Add move_app into `INSTALLED_APPS` in our `pokedex_proj/settings.py`

```python
  # pokedex_proj/settings.py
  INSTALLED_APPS = [
    "...",
    'move_app',
  ]
```

> Now Let's create a `Move` model in `move_app/models.py` and add a couple of validators to reinforce data constraints.

```python
# move_app/models.py

from django.db import models
from django.core import validators as v
from django.core.exceptions import ValidationError
from .validators import validate_move_name

# Create your models here.
class Move(models.Model):
    # We could use the same validator we created for the Pokemon Name for our Moves Name
    name = models.CharField(max_length=250, blank=False,
                            null=False, validators=[validate_move_name])
    # We want each move to have an accuracy between 1 and 100 percent and we will give it a default of 70%
    accuracy = models.PositiveIntegerField(
        default=70, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    # We want each move to have PP between 0 if they've utilized this move too much and 30 depending on it's max capability
    pp = models.PositiveIntegerField(default=20, validators=[
                             v.MinValueValidator(1), v.MaxValueValidator(30)])
    # We want to know just how much Power each move has
    power = models.PositiveIntegerField(
        default=80, validators=[v.MaxValueValidator(120)])

    def __str__(self):
        return f"| {self.name} | accuracy: {self.accuracy} | power: {self.power} | current_pp: {self.pp}/20 |"


# move_app/validators.py
from django.core.exceptions import ValidationError
import re

def validate_move_name(name):
    regex = r"^[a-zA-Z]+ ?[a-zA-Z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError("Improper Format")
```

> `makemigrations` and `migrate` this model.

```bash
  python manage.py makemigrations
  python manage.py migrate
```

> Create tests for both proper and improper input

```python
#move_app/tests.py
from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Move

# Create your tests here.
class move_test(TestCase):
    def test_01_create_move_instance(self):
        new_move = Move(name="Psychic")
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_02_create_move_with_incorrect_name_and_PP(self):
        new_move = Move(name="wing 4ttack", pp=25)
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue("Improper Format" in e.message_dict["name"])
```

> Now that we know our Model was created properly, we can create `serializers.py` and add a `serializer` for the Move model.

```python
#move_app/serializers.py
from rest_framework import serializers
from .models import Move

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'name', 'power', 'accuracy']
```

> To end this process Let's utilize the Django python shell to create a move and make some relationships.

```python
>>> from move_app.serializers import MoveSerializer
>>> psychic = MoveSerializer(data={"name":"Psychich"})
>>> psychic.is_valid()
True
>>> psychic.save()
<Move: | Psychich | accuracy: 70 | power: 80 | current_pp: 20/20|>
>>> psychic.data
{'id': 3, 'name': 'Psychich', 'power': 80, 'accuracy': 70}
```

> Perfect, now we have a pokemon Model and a move Model with a move instance. We can finally create some associations!

## Django ORM Associations

> As with database schema design, we can create relationships between our Django models to reflect certain requirements. Django provides some model fields to ease the relationship process:

### 1. OneToOneField

> The `OneToOneField` association represents a one-to-one relationship between two models. It is used when each instance of one model is related to exactly one instance of another model.

```python
class Person(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()
```

> In the example above, the `Profile` model has a `OneToOneField` named `person` that connects to the `Person` model. This means each `Profile` instance is associated with only one `Person` instance.

### 2. ForeignKey

> The `ForeignKey` association represents a many-to-one relationship between two models. It is used when each instance of one model can be associated with multiple instances of another model.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

> In the example above, the `Book` model has a `ForeignKey` named `author` that points to the `Author` model. This allows multiple `Book` instances to be associated with a single `Author` instance.

### 3. ManyToManyField

> The `ManyToManyField` association represents a many-to-many relationship between two models. It is used when each instance of one model can be associated with multiple instances of another model, and vice versa.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    # courses = created by the related_name relationship

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')
```

> In the example above, the `Course` model has a `ManyToManyField` named `students` that connects to the `Student` model. This allows multiple `Course` instances to be associated with multiple `Student` instances, creating a many-to-many relationship.

#### on_delete

> The on_delete=models.CASCADE option indicates that when the referenced object is deleted, all related objects will also be deleted. This means that if the referenced object is removed from the database, any related objects that depend on it will be automatically removed as well.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

> In the example above, the Book model has a foreign key relationship with the Author model. By specifying on_delete=models.CASCADE, when an Author instance is deleted, all associated Book instances will be deleted as well.

#### related_name

> The `related_name` parameter is used to establish a reverse relationship between models. It allows you to access related objects from the target model.

```python
class Person(models.Model):
    name = models.CharField(max_length=100)

class Pet(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='pets')
```

> In the example above, the `Person` model has a `ForeignKey` to the `Pet` model. By specifying `related_name='pets'`, we can access all the pets owned by a person using the reverse relationship.

```python
person = Person.objects.get(id=1)
pets = person.pets.all()  # Access all the pets owned by the person with id=1
```

> The `related_name` value should be unique and can be used in queries to retrieve related objects.

## Implementing Django Associations

> Let's take a look at how we could create a Many-To-Many relationship between our Pokemon Model and our Move Model:

```python
# pokemon_app/models.py

from move_app.models import Move
# Import the move model for us to make a relationship with

class pokemon(models.Model):
    #prior fields would go here and at the bottom of our model we would add any and all associations
    moves = models.ManyToManyField(Move, related_name="pokemon")
    # Creating a MANY pokemon to ONE move relationship and setting Code Platoon as the default value
```

> `makemigrations` and `migrate`.

```bash
  python manage.py makemigrations
  python manage.py migrate
```

> This many to many field we just created will be reflected in PostgreSQL within a separate data table named `pokemon_app_pokemon_moves` which will essentially act as a joint table for our database.

> Let's put this new association to the test by having both Eevee and Blastoise learn the move Psychic!

```python
>>> from pokemon_app.models import Pokemon # import the Pokemon model
>>> blastoise = Pokemon.objects.get(name = "Blastoise") # Retrieve Blastoise
>>> eevee = Pokemon.objects.get(name = "Eevee") # Retrieve Eevee
>>> blastoise.moves.all() # Just like we can do Pokemon.objects.all() we can see all the moves
<QuerySet []>
>>> blastoise.moves.add(1) # this many-to-many relationship is handled as a `set` within Django meaning that if we want to add a relationship we would do it through the `add` method
>>> blastoise.moves.all()
<QuerySet [<Move: | Psychich | accuracy: 70 | power: 80 | current_pp: 20/20|>]>
# Repeat the process for Eevee
>>> eevee.moves.all() 
<QuerySet []>
>>> eevee.moves.add(3)
>>> eevee.moves.all()
<QuerySet [<Move: | Psychich | accuracy: 70 | power: 80 | current_pp: 20/20|>]>
# save both of our Pokemon instances with their current changes.
>>> blastoise.save()
>>> eevee.save()
>>> exit()
```

> Many to Many relationships are treated as sets, meaning to add or remove from the set we must utilize the `add` or `remove` methods to alter the values within the set.

> Notice that we were able to access the `Move model` trough a specific pokemon instance, we could replicate this behavior through the `Move` instance by utilizing the related_name. `Move.pokemon.all()` Lets enforce this behavior through our `PokemonSerializer`

```python
# pokemon_app/serializers.py
from rest_framework import serializers
from .models import Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    moves = serializers.SerializerMethodField()
    # here we tell our serializer to utilize the method creating below to and place the methods return value into the 'moves' field. We only have to create a method because this is a many-to-many relationship. All other relationships would just take the model serializer instead of SerializerMethodField.
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'level', 'moves']

    def get_moves(self, instance):
        moves = instance.moves.all()
        move_names = [move.name for move in moves]
        return move_names
```

> If you'd like to learn more about serializers take a look at the [serializer guide](../CheatSheets/serializers.md)

```python
#move_app/serializers.py
from rest_framework import serializers
from .models import Move

class MoveSerializer(serializers.ModelSerializer):
    pokemon = serializers.SerializerMethodField()

    class Meta:
        model = Move
        fields = ['id', 'name', 'power', 'accuracy', 'pokemon']

    def get_pokemon(self, obj):
        pokemon = obj.pokemon.all()
        pokemon = [x.name for x in pokemon]
        return pokemon
```

> Enter the Python shell and look at your new serializer data for Blastoise

```python
>>> from pokemon_app.serializers import PokemonSerializer
>>> from pokemon_app.models import Pokemon
>>> blastoise = PokemonSerializer(Pokemon.objects.get(name = "Blastoise"))
>>> blastoise.data
{'id': 3, 'name': 'Blastoise', 'level': 37, 'moves': ['Psychich']}
```

> Congratulations we have successfully created and tested our Django Models with Associations. Let's dump the `Move` and `Pokemon` data and register our models onto the admin site

```bash
mkdir move_app/fixtures
python manage.py dumpdata move_app.Move --indent 2 > move_app/fixtures/moves_data.json
python manage.py dumpdata pokemon_app.Pokemon --indent 2 > pokemon_app/fixtures/pokemon_data.json
```

```python
  #move_app/admin
  from .models import Move

  admin.site.register([Move])
```

> run the server

```bash
  python manage.py runserver
```

and interact with our Models through the [Admin Site](http://localhost:800/admin)
