# Django API Views with Django Rest Frameworks

## Intro

So far we've created Pokemon and Moves utilizing Django-ORM with associations, validators, and tests. Although it's been great, we still haven't talked about why we are utilizing Django-ORM to interact with our database. Django is a powerful Back-End framework that we will utilize to host our Application Programming Interface for our Full-Stack-Applications. Today we are going to begin creating `url paths` and `views` that will allow other applications to ping our API to gather information from our Database. These `views` are known as `Model View Controllers (MVC's)` meaning they are `views` that will interact with our `models` and `control` the format our data will be returned to our application.

- [SLIDES](https://docs.google.com/presentation/d/1Yc5R7Gng_Fk0dHeuMRkiU6xI92jj0paVo9SyyfX5bRw/edit?usp=drive_link)

## What are Views?

> When it comes down to it, every Django view is a function. The biggest difference is this function takes an HTTP request object in JSON format and returns an HTTP response object in JSON format. Views in Django can do many things: render HTML templates, interact with the Database, redirect to a separate url, handle errors, etc.

## Things to consider when creating our API Views

1. Using JSON format to send and receive data.
   - This is because most Frameworks now a days (Front-End or Back-end) have built in methods to effectively utilize JSON data. JSON was specifically made to interact with JavaScript and is therefor easily interpreted by JavaScript. Python has a built in methods like `json.loads()` to grab the JSON data in the body of a request and turn it into something Python can utilize.
   - Luckily thanks to Django Rest Framework, we won't have to interact much with complicated methods and serializers. Instead we could just use the `serializers` we've created with `rest_framework` and allow DRF to handle any data formatting for JSON AND/OR XML.
2. Use Filtering and Sorting to Retrieve the Data Requested.
   - Databases can get very large and complicated so it's important to only grab the necessary data from our database and sort it to create consistency in our API responses.

## Linking urlpatterns

> To create our API CBV's we will utilize [django-rest-frameworks APIViews and Responses](https://www.django-rest-framework.org/) to interact with our requests and deliver effective responses.

> Lets cover how to link our app urls onto our project urls. We already know interactions with the Django Web Server come through `urlpatterns` their `paths` and corresponding `views`. Yesterday we did a quick intro to the Django server but never actually linked our URL paths to our project.

> RESTful API design dictates a certain structure to follow for URL patterns. Each `url` in a `path` must specify it's an API endpoint by including `api/` immediately after the hosting IP address in the url. The `api/` url is then followed by the current version number of the API which in this case it will be `v1` since it's our first version. Lastly the url pattern is followed by a pluralized noun that describes the `Model` this paths `view` will interact with.

> Yesterday we created a series of url paths within our `pokedex_proj.urls` and it worked great, but, just like everything in programming, we don't want to place all possible url paths within this one file. Instead we want to divide the load and use our paths in `pokedex_proj.urls` to connect us to other apps urls and views (This is another way of following the Single Responsibility Principle). Link `project.urls` to individual `app.urls` by using Django's `include()` and pass in the path in dot notation to the `urls.py` file of that app.

```python
# import include to access different apps urls.py
from django.urls import path, include

# enpoints should be nouns and pluralized
urlpatterns = [
    path('admin/', admin.site.urls),
    path('squares/', square_area_view, name='square'),
    path('circles/', circle_area_view, name='circle'),
    path('triangles/height/<int:height>/base/<int:base>/', triangle_area_view, name='triangle'),
    path("api/v1/pokemon/", include("pokemon_app.urls")),
]
```

> We are telling our project to include pokemon_app/urls.py, but there is no urls.py file in our pokemon_app. Lets make one and add a `urlpattern` with an empty path.

```python
# pokemon_app/urls.py
from django.urls import path
# Explicit imports
from .views import all_pokemon
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path('', all_pokemon, name='all_pokemon')
]
```

> Currently if we attempt to run the Django Server we will receive an error stating there's no `view` named `all_pokemon` in `pokemon_app.views`. Well let's fix that.

## Creating MVC's

> Go into pokemon_app/views.py to create our API view that will get all of our existing pokemon from the database and return them in the correct `JSON` format. Here's an example of what we would expect it to look:

```JSON
{
    "pokemon": [
        {
            "id": 3, 
            "name": "Blastoise", 
            "level": 37, 
            "moves": [
                "Psychich"
            ]
        }, 
        {
            "id": 2, 
            "name": "Charizard", 
            "level": 25, 
            "moves": []
        }, 
        {
            "id": 4, 
            "name": "Eevee", 
            "level": 25, 
            "moves": [
                "Psychich"
            ]
        }, 
        {
            "id": 1, 
            "name": "Pikachu", 
            "level": 12, 
            "moves": []
        }
    ]
}
```

> Create the following Functional View:

```python
#pokemon_app/views.py
from .models import Pokemon #imports the Pokemon model
from .serializers import PokemonSerializer #imports the PokemonSerializer
from django.http import JsonResponse # Our responses will now be returned in JSON so we should utilize a JsonResponse
# Create your views here.

def all_pokemon(request):
    pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True) # Utilize the serializer to serialize all of our Pokemon pulled from the Database
    return JsonResponse({"pokemon": pokemon.data}) # JSON could only be interpreted in dictionary format so we need to ensure our response is a dictionary itself.
```

> Make sure it works by opening a browser on [http://127.0.0.1:8000/api/v1/pokemon/](http://127.0.0.1:8000/api/v1/pokemon/). You should see a page with raw JSON displaying the information we desire.

> This Functional View works but as a function it's capabilities are limited and we can see that any type of request (POST/GET/PUT/DELETE) being sent to this url will receive the same response and we should only send this response to a `GET` request. Well we can utilize DRF's `APIView` to exchange our Functional View for a Class Based View and essentially `evolve` our views capabilities and limitations.

```python
# pokemon_app/views.py
from .models import Pokemon
from .serializers import PokemonSerializer
# Import both APIView and Response from DRF
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# def all_pokemon(request):
#     pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True)
#     return JsonResponse({"pokemon": pokemon.data})

# We can create this class and pass in APIView as the Parent Class to allow DRF to handle permissions, authentications, and allowed methods.
class All_pokemon(APIView):
    # Just like we said before we only want this information available for GET requests therefore we have to place this logic under a GET method. DRF will recognize the `get` method and trigger that method every time a GET request is sent
    def get(self, request):
        pokemon = PokemonSerializer(Pokemon.objects.order_by('name'), many=True)
        # Under response we don't necessarily need to send information in JSON format instead DRF will format our response and make it acceptable for Front-End frameworks
        return Response(pokemon.data)
```

> Next we have to fix our `pokemon_app.urls` url patterns to use this Class Based View we've just created.

```python
#pokemon_app.urls
from .views import All_pokemon
# Remember all urls are prefaced by http://localhost:8000/api/v1/pokemon/
urlpatterns = [
    # Currently only takes GET requests
    path('', All_pokemon.as_view(), name='all_pokemon')
]
```

> Notice we are following our Class Based View with a built in method `as_view`... but why? The reason for using .as_view() is because class-based views in DRF are designed to be more flexible and customizable compared to function-based views. When a request comes in, Django's URL dispatcher expects a callable view function that takes a request as its argument and returns an HTTP response. However, class-based views are not callable by default, so .as_view() is used to make them callable and compatible with the URL routing system.

> When you use .as_view() in your URL patterns, it instantiates an instance of your class-based view and provides the necessary handling to ensure that the appropriate methods (such as get(), post(), etc.) are called based on the incoming request's HTTP method. This allows you to define separate methods for different HTTP methods within your class-based view, providing a more organized and structured way of handling requests.

> We made quite a bit of changes to our Django API already but not just in our logic. Go to [http://127.0.0.1:8000/api/v1/pokemon/](http://127.0.0.1:8000/api/v1/pokemon/) and you'll notice DRF has now provided a template that will render our Django Response in a `prettier` format than RAW JSON.

### All Moves

> We have a working `GET` method for all pokemon in our database let's replicate this behavior for pokemon moves by following these steps.

`project.urls => app.urls => app.views`

> Link app.urls with project.urls by utilizing the `include()` method.

```python
from django.contrib import admin
# import include to access different apps urls.py
from django.urls import path, include

urlpatterns = [
    "...",
    path('api/v1/pokemon/', include("pokemon_app.urls")),
    path('api/v1/moves/', include("move_app.urls")),
]
```

> Link our move_app/urls.py with our CBV

```python
#move_app/urls.py
from django.urls import path
from .views import All_moves

urlpatterns = [
    path("", All_moves.as_view(), name='all_moves')
]
```

> We now get an error along the lines of `All_moves` does not exist in .views. Well lets make it.

```python
from .models import Move
from .serializers import MoveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create a view that utilizes APIView to inherit DRF's built in functionality
class All_moves(APIView):
    # establish a get method that will be triggered by GET requests
    def get(self, request):
        # utilize your ModelSerializer to serialize your queryset and return a proper response with DRF's Response
        moves = MoveSerializer(Move.objects.all(), many=True)
        return Response(moves.data)
```

> This CBV should return the following:

```JSON
[
    {
        "id": 1,
        "name": "Psychich",
        "power": 80,
        "accuracy": 70,
        "pokemon": [
            "Blastoise",
            "Eevee"
        ]
    }
]
```

> Make sure it works by opening a browser on [http://127.0.0.1:8000/api/v1/pokemon/](http://127.0.0.1:8000/api/v1/moves/). You should see DRF's template displaying our JSON data.
