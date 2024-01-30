# Django Serializers

## Intro

> Django serializers are a powerful tool provided by the Django web framework to convert complex data types, such as Django model instances, into JSON, XML, or other content types. They also allow deserialization, converting the received data back into complex types after first validating the incoming data.

> Serializers play a crucial role in Django's REST framework, where they are used to handle requests and responses. In this guide, we'll explore the fundamentals of Django serializers and how to use them effectively.

## Django Rest Frameworks (DRF)

> Django Rest Framework (DRF) is a versatile toolkit that enhances Django's capabilities for building Web APIs. It achieves this by providing a comprehensive set of features and utilities. DRF simplifies API development by offering tools for defining endpoints, handling requests, and formatting responses. It accomplishes serialization through a robust framework that facilitates the conversion of complex data types into various content types. DRF handles requests by offering view classes and function-based views that map URLs to specific actions. It ensures secure API access through authentication schemes and a flexible permission system. DRF includes built-in pagination classes to handle large data sets effectively. It enforces data validation rules for incoming requests through a comprehensive validation framework. Additionally, DRF enhances the developer experience by providing a browsable API feature for easy exploration and debugging. Finally, DRF includes testing utilities and helpers to simplify the testing of API views, serializers, and authentication. Overall, Django Rest Framework empowers Django developers to build powerful and scalable APIs with ease and efficiency.

> click [here](../../../Resources/Why_DRF.md) to learn more about DRF

## Why Use Serializers?

- **Serialization**: Serializers help convert complex data types (e.g., models, querysets) into easily renderable formats like JSON or XML.
- **Deserialization**: Serializers allow the parsed data to be converted back into complex types after validating the incoming data.
- **Validation**: Serializers automatically validate the data against the model's fields and raise appropriate validation errors if necessary.
- **Support for Relationships**: Serializers handle relationships between models, allowing nested data representation and manipulation.

## Serializing Data

### Using Django Serializers

> Django core definitely provides the capability to serialize our data and turn our QuerySet onto a JSON readable format that we can "easily" work with. Well lets take a look at how Django handles this behavior by serializing our `Blastoise` Pokemon instance:

```python
python manage.py shell
>>> from pokemon_app.models import Pokemon
>>> blastoise = Pokemon.objects.get(name = "Blastoise")
>>> print(blastoise)
Blastoise is yet to be caught
```

> Good, up to this point we have imported our `Pokemon` model from `pokemon_app.models` and then grabbed `Blastoise` as a QueryObject from our PostgreSQL database. Now when we print blastoise we can see our `__str__` method taking over and displaying a string on our Python shell. Although this is useful to us as developers, eventually we will want to communicate with a Front-End framework(React) and to do so we need to handle said communication in json format. That's where our Django Core Serializers come in:

```python
>>> from django.core.serializers import serialize # Import serialize function from Django Core Serializers
>>> blastoise_serialized = serialize("json", [blastoise])
# Serialize takes in two REQUIRED arguments:
# 1. The format in which it should serialize the data to (in this case "json")
# 2. An iterable object holding instances of information to be serialized
# In our example we are only serializing blastoise and blastoise is not ITERABLE. To fix this
# we wrap it within a List to allow the serialize function to iterate through the list and 
# serialize the one object
>>> blastoise_serialized
'[{"model": "pokemon_app.pokemon", "pk": 3, "fields": {"name": "Blastoise", "level": 37, "date_encountered": "2008-01-01", "date_captured": "2023-08-22T15:28:54.699Z", "description": "Unknown", "captured": false}}]'
# Finally we see a serialized object appear on the console as a List holding the Blastoise Pokemon dictionary
```

> Now this may seem like List and a Dictionary, but, remember we just serialized our data onto JSON (a language applicable to JavaScript but not Python). This means that if we try to do something like `blastoise_serialized[0].get("pk")` to get our Pokemons Primary Key(PK) we would receive an error since Python treats JSON as plain string. To fix this issue, Python utilizes the `json` library to interpret JSON objects and turn them into equivalent Python Data Types. For example:

```python
>>> blastoise_serialized[0].get("pk")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'str' object has no attribute 'get'
>>> import json
>>> json_blastoise = json.loads(blastoise_serialized)
>>> blastoise[0].get("pk")
3
```

> Now we created a Python Object that we can work with to manipulate values and possibly send said values to our Front-End Framework.

> I'm sure you've realized this is quite a bit of work and there has to be a better way of doing this. Well that's where Django Rest Frameworks comes in.

### DRF Model Serializers

> Before we can start using the tools of Django Rest Frameworks, we have to install DRF and add it to our Django Settings Installed Apps.

```bash
# TERMINAL
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
  "....",
  "pokemon_app",
  "rest_framework",
  "..."
]
```

> Model serializers are a shortcut in Django for automatically determining the serializer fields based on the model definition. They provide a simple way to serialize and deserialize model instances.

> To create a model serializer, you need to define a class that inherits from `serializers.ModelSerializer`. The serializer class's `Meta` inner class specifies the model and fields to include in the serialization process.

> Lets create a `serializers.py` and create a serializer for our `Pokemon Model`:

```python
# pokemon_app/serializers.py
from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.
```

> Lets open up the Django Python Shell and take a look at how our serializer works

```python
>>> from pokemon_app.models import Pokemon #import Pokemon model
>>> from pokemon_app.serializers import PokemonSerializer #import Pokemon Serializer
>>> pikachu = Pokemon.objects.get(id = 1) # Grab Pikachu from db
>>> pikachu
<Pokemon: Pikachu has been captured> # This is what Pikachu looks like when printed from a query set
>>> pikachu_serializer = PokemonSerializer(pikachu)
>>> pikachu_serializer # Here is the same Pikachu with the specified fields we provided
PokemonSerializer(<Pokemon: Pikachu has been captured>):
    id = IntegerField(label='ID', read_only=True)
    name = CharField(max_length=200, validators=[<function validate_name>])
    level = IntegerField(max_value=100, min_value=1, required=False)
>>> pikachu.name #We can utilize dot notation because pikachu is still a class instance
'Pikachu'
>>> pikachu_serializer.name #Notice this throws an error because our data is now in json format meaning we are now interacting with a dictionary and not a class
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'PokemonSerializer' object has no attribute 'name'
>>> pikachu_serializer['name'] # We call the key of name and get Pikachu's name returned
<BoundField value=Pikachu errors=None>
>>> pikachu_serialized.data # Inside of our Serializers data attribute we can see a fully readable and easy to work with Pokemon dictionary (which also translates to JSON)
{'id': 1, 'name': 'Pikachu', 'level': 12}
>>> exit()
```

### Serializing QuerySets

> Serializers can also handle querysets, allowing you to serialize multiple objects at once. To achieve this, you can pass a queryset instance to the serializer's `many=True` argument.

```python
all_pokemon = Pokemon.objects.all()
serializer = PokemonSerializer(all_pokemon, many=True)
```

### Creating an Object

> To create a new object from deserialized data, you can call the serializer's `save()` method.

```python
>>> from pokemon_app.serializers import PokemonSerializer # import PokemonSerializer from pokemon_app/serializers.py
>>> eevee = {"name":"Eevee", "level": 25} # we can make a dictionary with the required information we would like
>>> ser_eevee = PokemonSerializer(data = eevee) # by passing the dictionary into the serializer we allow the is_valid() check if the dictionary data fits our validators essentially replacing Djangos built in full_clean() function
>>> ser_eevee.is_valid()
True
>>> ser_eevee.save() # .save() still creates a new db entry and class instance even though it's from the PokemonSerializer class
<Pokemon: Eevee is yet to be caught>
```

> It's important to note that serializers automatically validate the incoming data against the model's fields before saving any data onto our database.
