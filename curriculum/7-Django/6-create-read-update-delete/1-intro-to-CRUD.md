# Intro to CRUD

## Intro

In this lesson we will cover basic Create Read Update and Delete (CRUD) principles and fundamentals while creating our own UPDATE method in our Pokedex project.

## What is CRUD

> CRUD stands for Create, Read, Update, and Delete. It is a commonly used acronym in software development and database management, referring to the four basic functions that are essential for working with persistent data.

> Create refers to the process of adding new data to a system, such as creating a new record in a database or adding a new item to a list.

> Read refers to the process of retrieving existing data from a system, such as querying a database to retrieve a specific record or displaying a list of items. We have done this through our previous lessons by sending `GET` requests to our Django Back End through Thunder Client.

> Update refers to the process of modifying existing data in a system, such as editing a record in a database or updating the details of an item.

> Delete refers to the process of removing existing data from a system, such as deleting a record from a database or removing an item from a list.

> Together, these four operations provide a foundation for managing data in a wide range of applications and systems.

## CRUD in API Design

> The Hypertext Transfer Protocol (HTTP) is a protocol for distributing content that provides a set of methods to declare actions. By convention, REST APIs rely on these methods and it's important to use the appropriate HTTP method for each type of action:

| Purpose of Request          | HTTP Method | Rough SQL equivalent | HTTP Response Status                     |
| --------------------------- | ----------- | -------------------- | ---------------------------------------- |
| Create a new resource       | POST        | INSERT               | 201 Created                              |
| Read an existing resource   | GET         | SELECT               | 200 Success /404 Not Found               |
| Update an existing resource | PUT         | UPDATE               | 204 / 200 if something is being returned |
| Delete an existing resource | DELETE      | DELETE               | 204 No content                           |

## Why request.data?

> So far our application has full READ capabilities but we don't have a way to UPDATE, CREATE, OR DELETE information from our database through our API views. In this lesson we will concentrate on the `update` method and integrate it with our pokedex project by giving users the ability to change a Pokemons level, captured status, description, moves and type.

> We have seen how to pass parameters through `url paths` but we haven't talked about other methods of receiving information from a user. If we attempted to send all the parameters of a Pokemon through a `url path` we would end up with something ridiculous like this:

```python
path("pokemon/<int_or_sting:name_or_id>/name/<str:name>/level/<int:level>/captured/<str:status>/move1/<int:move1_id>/move2/<int:move2_id>/move3/<int:move3_id>/move4/<int:move4_id>/")
```

> We don't want all of these options to be integrated onto our `url paths`, instead we will have users send this information through requests data. Every `request` made to a server comes with an attribute named `body` and is typically interpreted as `binary string`, but, because we are using DRF, that `body` is "translated" into a JSON readable dictionary that Python can interact with and placed within the request under a new header/attribute named `data`.

## Implementing the PUT method

> We already have a `A_pokemon` API view in our `pokemon_app.views` that can successfully `GET` a pokemon from our database by either name or id and return it in a Response. Now that we want to UPDATE something in the database we will utilize the `PUT` request method to trigger our next set of behavior.

```python
# pokemon_app/views.py
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST

    def put(self, request, id):  # <-- This should be a direct reflection from the get method
        # we still want to grab a pokemon either by ID or by name so lets grab that behavior from the get method as well
        if type(id)==int:
            pokemon = Pokemon.objects.get(id = id)
        else:
            pokemon = Pokemon.objects.get(name = id.title())
        # Now we have to check the body of our request and check if
        # the following keys are in our request ['level_up', 'captured', 'moves', description]
        if 'level_up' in request.data and request.data['level_up']:
            pokemon.level_up()
        if 'captured' in request.data and type(request.data['captured']) == bool:
            pokemon.change_caught_status(request.data.get("captured"))
        if "moves" in request.data:
            pokemon.moves.add(request.data.get("moves"))
        if "description" in request.data and request.data.get("description"):
            pokemon.description = request.data.get("description")
        if "type" in request.data and request.data.get("type"):
            pokemon.type = request.data.get("type")
        # Add pokemon to our PokemonSerializer to validate data
        ser_pokemon = PokemonSerializer(pokemon, data = vars(pokemon))
        # lines 60 - 71 check each individual field for the request.data to find out what it can
        # change within the Pokemon instance... but there's gotta be a better way of doing this...
        # well our DRF Model Serializer can actually handle partial data and check each individual 
        # field for us instead of having us check it manually. Please utilize the example below:
        ser_pokemon = PokemonSerializer(pokemon, data = request.data, partial = True)
        if ser_pokemon.is_valid():
            # save all changes
            ser_pokemon.save()
            # We've made our necessary changes to the pokemon instance so we can return the appropriate response status of 204 which we will grab from DRF
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            print(ser_pokemon.errors)
            return Response(ser_pokemon.errors, status=HTTP_400_BAD_REQUEST)

# In the example above we are attempting to utilize our Serializer to validate all the new data... but currently our serializer only tracks on some fields not all. Lets update our PokemonSerializer to include all fields

# pokedex/backend/pokemon_app/serializers.py

fields = "__all__"
```

> We've built out our `PUT` method and return the appropriate response. This CBV is still linked to the same `url path` that our `GET` method was linked to. The only difference is we now have the ability to send both `PUT` and `GET` requests to the same url pattern.

> Everything is working properly but I'm starting to notice that I have a bit of repeated code within my `A_pokemon` CBV. I want to ensure I don't repeat myself so I think I'm going to go back and apply a django shortcut name `get_object_or_404` and create a method that will return a pokemon instance.

```python
    # create a method that you can utilize through out the entire class
    def get_a_pokemon(self, id):
        pokemon = None
        if type(id) == int:
            pokemon = get_object_or_404(Pokemon, id = id)
        else:
            pokemon = get_object_or_404(Pokemon, name = id.title())
        return pokemon

    # `get_object_or_404` is a method that takes in two arguments. first the method it's looking into and second the conditions it's looking for. This method will return the specific Model instance we are looking for if it exists. If it doesn't find the Model instance that meets our conditions, it will immediately return a 404 error saving us time and server space.

    def get(self, request, id):
        pokemon = self.get_a_pokemon(id) # utilize newly created method

    def put(self, request, id):
        pokemon = self.get_a_pokemon(id) # utilize newly created method
```

## Testing PUT views

> Now that we have created our `PUT` method MVC, we want to be able to test it and ensure everything is working correctly through out the development process.

```python
# tests/test_views.py

# ensure names are specific to what's going on in the test
def test_003_update_pokemon_data(self):
        updated_pokemon = Pokemon(name="Eevee")
        updated_pokemon.save()
        # Theres a couple of differences in the way we send this request through our client.
        # 1. Notice that our client is specifically sending a PUT request to our URL
        # 2. We are no passing a data parameter holding a dictionary that will be passed to the request
        # 3. By default Django send "application/octet-stream" data in tests so we have to specify that
        #    we are sending "application/json" data in content_type
        response = self.client.put(
            reverse("a_pokemon", args=["eevee"]),
            data={
                "level_up": True,
                "captured": True,
                "description": "This is Pikachu and it is a surprizingly weak electric type that does not live up to it's name",
            },
            content_type="application/json",
        )
        # We don't have response content to assert so instead we will assert the HTTP status_code
        self.assertEquals(response.status_code, 204)
```
