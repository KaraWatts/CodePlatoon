# Custom Endpoints and Testing

## Intro

By the end of this lesson we will have a better understanding of flexible API endpoints and how to implement tests to both urls and views.

- [SLIDES](https://docs.google.com/presentation/d/1gQKE6PeUa2CiKqJpPm0Ksg4mxkKTcl-jc7-HSSMYxco/edit?usp=drive_link)

## Expanding Endpoints

> Lets Expand on our current endpoints and create the ability to grab a single instance from our database. In order for a user to request a specific pokemon instance, we need to give our user a way to give us information either through the body of the request or through the URL itself by passing in url parameters. Django has a two built in parameter types we can add to our URL's: `str`, `int`.

> String parameters are passed through Django URL's in the following format `<str:variable>`. The left side defines the type of the variable we are receiving which in this case it's a `string` type, and the right side declares the variable name that our APIView methods can use to reference the url input. The same goes for Integer parameters the only difference is the left side would be `int` enforcing the type of the parameter.

```python
    # In this case we are telling Django that after '...pokemon/' we will receive an '...pokemon/interger/' and it will be ended by a slash
    int_path = 'http://127.0.0.1:8000/api/v1/pokemon/<int:id>/' 
    # 1, 22, 176 ACCEPTABLE) | Blastoise, Pikachu (UNACCEPTABLE)

    str_path = 'http://127.0.0.1:8000/api/v1/pokemon/<str:id>/' 
    # 1, 22, 176 (ACCEPTABLE) | Blastoise, Pikachu (ACCEPTABLE)
```

> Now what if I need my API to be flexible and be able to take in both int or string and return the correct data type? Well Django doesn't provide me with that option. So lets create a custom "type" for our parameter that will take in both str or an int type.

> Create a converters.py file in the pokemon_app and add the following converter class.

```python
# pokemon_app/converters.py

class IntOrStrConverter:
    regex = '[0-9]+|[a-zA-Z]+'

    def to_python(self, value):
        if value.isdigit():
            return int(value)
        else:
            return str(value)

    def to_url(self, value):
        return str(value)

```

> It's important we don't just copy and paste code so lets take a pause here and break down what we want this converter to do when interacting with views and url patterns:

```python
class IntOrStrConverter:
    regex = '[0-9]+|[a-zA-Z]+'
```

> `regex = '[0-9]+|[a-zA-Z]+'`: The regex attribute defines a regular expression pattern that specifies the allowed format for the parameter value. In this case, it allows for either one or more digits ([0-9]+) or one or more letters ([a-zA-Z]+).

```python
    def to_python(self, value):
        if value.isdigit():
            return int(value)
        else:
            return str(value)
```

> to_python(self, value): This method is responsible for converting the captured URL parameter value to its corresponding Python object. It is called during the URL parsing process.

> if value.isdigit(): return int(value): This condition checks if the value is composed of only digits. If so, it converts the value to an integer using int(value).

> else: return str(value): If the value contains non-digit characters, it treats the value as a string and returns it as is.

```python
    def to_url(self, value):
        return str(value)
```

> to_url(self, value): This method is responsible for converting the Python object back to its string representation. It is called when generating URLs using the reverse() function or url template tag.

> return str(value): The method simply converts the Python object value to a string using str(value) and returns it.

> In the background, Django uses these methods to handle the conversion between URL parameter values and Python objects. When a URL is matched against a pattern that uses the IntOrStrConverter, Django will utilize the to_python() method to convert the captured value into the appropriate Python object. When generating URLs, Django will use the to_url() method to convert the Python object back to its string representation.

> Now we can import this class into pokemon_app/urls.py and register it as a converter for url parameters as such

```python
#pokemon_app/urls.py
# import register converter to create new param types in URL patterns
from django.urls import path, register_converter
# Explicit imports
from .views import All_pokemon, A_pokemon
# import our converter class to utilize as a parameter type
from .converters import IntOrStrConverter

# To use this custom converter in a URL pattern, you need to register it with Django using the register_converter function.
register_converter(IntOrStrConverter, 'int_or_str')
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path('', All_pokemon.as_view(), name='all_pokemon'),
    # now we can utilize our converter for the variable we provided
    path('<int_or_str:id>/', A_pokemon.as_view(), name='a_pokemon')
]
```

> We have a url pattern established and created a `type converter` for a url parameter... but how does that connect to our views? In pokemon_app/views lets create an `A_pokemon` CBV that will take in a get request and the id or name of the pokemon the user is looking for and returns an individual pokemon instance.

```python
# pokemon_app/views

class A_pokemon(APIView):
    
    #  Specify the method to trigger this behavior
    def get(self, request, id): # <-- Notice id is now a parameter and its value is being pulled straight from our URL
        # Lets initialize pokemon as None and give it a
        # corresponding query set depending on the ids type
        pokemon = None
        if type(id) == int: # the to_python method from the converter will return the correct type here
            pokemon = Pokemon.objects.get(id = id)
        else:
            pokemon = Pokemon.objects.get(name = id.title()) # <== We only accept names in Title format so lets use the `title` method to ensure we have the user input in the correct format
        return Response(PokemonSerializer(pokemon).data) #<=== Finally lets use the PokemonSerializer to return our Pokemon in the correct Format for Front End frameworks
    
```

> Users can now get a single pokemon instance by either passing a pokemon name or pokemon ID! Now lets create a url path and view for grabbing a single pokemon move by name.

```python
# move_app/urls.py
from django.urls import path
from .views import All_moves, A_move

urlpatterns = [
    path('', All_moves.as_view(), name='all_views'),
    path("<str:name>/", A_move.as_view(), name="a_move"),
]
```

> Now we can create the `A_move` class and take in the name parameter

```python
# move_app/views.py
class A_move(APIView):
    def get(self, request, name):
        move = Move.objects.get(name = name.title())
        return Response(MoveSerializer(move).data)
```

> Our user is now able to grab all pokemon, all moves, a pokemon, or a move through our API! Now lets create some tests to ensure that our future refactoring does not break our application.

## Testing our API endpoints

> Now that we have some extensive data and relationships created, we will want to utilize fixtures in our tests to mimick our current data available from our Database. Create some fixtures using `dumpdata` onto each app.

> As we can see our App's are becoming more and more complex as their relationships grow. In order to test them both correctly we will have to do a bit of folder restructure. So let's get started:

- On the same level as your apps and project create a new directory called `tests`
- Inside of tests create a file `test_models.py` and move all of our pre-existing tests onto this file. Once you've done that you could delete the tests.py file in each app.

```python
 # tests.test_models
from django.test import TestCase
from django.core.exceptions import ValidationError
from pokemon_app.models import Pokemon, Move # import pokemon model

# Create your tests here.
class pokemon_test(TestCase):
    
    def test_01_create_pokemon_instance(self):
        # Here we will create our pokemon instance
        new_pokemon = Pokemon(name="Pikachu", description = 'Only the best electric type pokemon in the show but NOT in the games')
        try:
            # remember validators are not ran on our new instance until we run full_clean
            new_pokemon.full_clean()
            # here we will ensure our instance is actually created
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            # print(e.message_dict)
            #if it sends an error we want to ensure this test fails
            self.fail()
        
    def test_02_create_pokemon_with_incorrect_name_format(self):
        # we create an instance with an improper name
        new_pokemon = Pokemon(name='ch4r1z4 rd', description = 'Looks like a Dragon has wings, breathes fire.. but is not a dragon')
        try:
            new_pokemon.full_clean()
            # if our instance runs through the full clean and doesn't throw an error, than we
            # know our validator is not working correctly and we should fail this test 
            self.fail()

        except ValidationError as e:
            # print(e.message_dict)
            # we can ensure the correct message is inside our ValidationError
            self.assertTrue('Improper name format' in e.message_dict['name'])

# Create your tests here.
class move_test(TestCase):
    def test_03_create_move_instance(self):
        new_move = Move(name="Psychic")
        try:
            new_move.full_clean()
            self.assertIsNotNone(new_move)
        except ValidationError as e:
            # print(e.message_dict)
            self.fail()

    def test_04_create_move_with_incorrect_name_and_PP(self):
        new_move = Move(name="wing 4ttack", pp=25)
        try:
            new_move.full_clean()
            self.fail()
        except ValidationError as e:
            # print(e.message_dict)
            self.assertTrue("Improper Format" in e.message_dict["name"])
```

- Inside the tests directory create a test_views.py and an answers.py
- Fill in answers.py with the results we receive from pinging our API endpoints. This way we can import the information onto our test files to ensure it stays consistent.

```python
a_pokemon = {"..."}

a_move = {"..."}

all_pokemon = ["..."]

all_moves = ["..."]
```

- In test_views.py we can create tests to ensure our views are producing the desired behavior.

```python
# tests/test_views.py

# A client must ping our api in order for our views to be triggered.
from django.test import TestCase, Client
# We can't make calls ourselves to this api so we will utilize reverse to mock this behavior
from django.urls import reverse
# we can import all the expected answers from our answer.py file
from tests.answers import all_pokemon, a_pokemon, all_moves, a_move
import json


class Test_views(TestCase):
    # We dont have a database so we will mock our DB through fixtures
    fixtures = [
        "pokemon_data.json",
        "moves_data.json"
    ]
    # We will need a client for every test, instead of re-writing  this
    # instance we can use the set up method to access the client on every
    # test by prepending it with self
    def setUp(self):
        client = Client()

    def test_001_get_all_pokemon(self):
        # client sends a get request to a url path by url name
        response = self.client.get(reverse('all_pokemon'))
        response_body =json.loads(response.content)
        # we want our responses body to be equal to our answer from answer.py
        self.assertEquals(response_body, all_pokemon)

    def test_002_get_a_pokemon(self):
        # client sends a get request to a url path by url name.
        response = self.client.get(reverse('a_pokemon', args=['pikachu']))
        # since our URL has an integrated parameter, we can pass it's value through args
        response_body = json.loads(response.content)
        self.assertEquals(response_body, a_pokemon)
    # REPEAT THE PROCESS FOR THE MOVE_APP
```

- Create a test_urls.py where we can ensure the correct path and view is attached to each url.

```python
# tests/test_urls.py
from django.test import TestCase
# We need reverse to be able to ping our own urls by name
# resolve will give us detailed information about our url
# such as routes, args, views, and more
from django.urls import reverse, resolve
# We will want to have all the views we've created to
# ensure they match with their corresponding url
from pokemon_app.views import All_pokemon, A_pokemon
from move_app.views import All_moves, A_move


class Test_urls(TestCase):

    def test_001_all_pokemon(self):
        # we will resolve our url to access the information attached to the
        # url instead of seeing it's behavior
        url = resolve(reverse('all_pokemon'))
        # subTest allows us to run more than one assertion within a Test
        with self.subTest():
            # Here we will ensure the url path matches the url route
            self.assertEquals(url.route, 'api/v1/pokemon/')
        # Finally we will assert the correct view is corresponding to this endpoint
        self.assertTrue(url.func.view_class is All_pokemon)

# DO THE SAME FOR REMAINING ENDPOINTS
```

- Now we can run the test suite and watch all 12 of our existing test pass or fail. Currently we know our API is working the way we want it too up to this point, so if a test fails adjust it to fit your behavior. Once adjusted, tests shouldn't be touched again since they are our easiest way of ensuring our application is continuously working as desired.

```bash
    python manage.py test tests
```
