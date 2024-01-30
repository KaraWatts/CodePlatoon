# Django Server

## Intro

In this lesson we are going to step away from the `Pokedex` exercise for a second and concentrate on the Django Server. The Django server is a development server that allows you to run your Django web application locally for testing and development purposes. It provides a convenient way to preview your application and debug any issues before deploying it to a production environment. This guide covers several important topics related to the Django server:

1. [What does `python manage.py runserver` do?](#what-does-python-managepy-runserver-do)
2. [How do urlpatterns and paths work?](#how-do-urlpatterns-and-paths-work)
3. [How do URL paths link to Django views?](#how-do-url-paths-link-to-django-views)
4. [What is a request?](#what-is-a-request)
5. [How to pass parameters through URL patterns?](#how-to-pass-parameters-through-url-patterns)

## What does `python manage.py runserver` do?

> The `python manage.py runserver` command is used to start the Django development server. It launches a lightweight web server that listens for incoming requests and serves your Django application locally. By running this command in your project's root directory, you can access your application via a local URL (typically `http://127.0.0.1:8000/`) in your web browser.

## How do urlpatterns and paths work?

> In Django, the `urlpatterns` variable is a list of URL patterns defined in your project's `urls.py` module. Each URL pattern consists of a `path()` function call, which maps a URL pattern to a specific view function or view class.

> The `path()` function takes two required arguments: `route` and `view`. The `route` argument specifies the URL pattern, while the `view` argument identifies the view function or class that handles the request.

```python
# pokedex_proj/urls.py

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('squares/', square_area_view, name='square'),
    # path('circles/', circle_area_view, name='circle'),
    # path('triangles/', triangle_area_view, name='triangle'),
]
```

> In the example above, three URL patterns are defined. The first pattern maps the URL `squares/` to the `square_area_view` function, and the second pattern maps the URL `/circles/` to the `circle_area_view` function and so on.

> It's important to note that each one of these URL paths are prefaced by `http://127.0.0.1:8000/`, this means that if we wanted to send a request to the `squares/` path we would have to send a request to `http://127.0.0.1:8000/squares/`

## How do URL paths link to Django views?

> URL paths in Django are associated with view functions or view classes, we will learn about Class Based Views later on in the course. When a request is made to a specific URL, Django's URL resolver determines the corresponding view function or class based on the defined URL patterns.

> For example, if a user requests the URL `squares/`, Django's URL resolver matches it to the `square_area_view` function specified in the `urlpatterns` list. Currently this view function doesn't exist, so lets create it right above our `urlpatterns`. (This is not where views should be created but for simplicities sake this is where we will create them today)

```python
# pokedex_proj/urls.py
from django.http import HttpResponse

def square_area_view(request):
    area_of_a_square = 2 ** 2
    return HttpResponse(area_of_a_square)

urlpatterns = [
    path("..."),
]
```

> The `square_area_view` function is responsible for processing the request and generating an appropriate response. It can interact with models, perform calculations, and render templates to construct the response.

> Lets try this out by running our Django Server with `python manage.py runserver` and then opening our browser with [http://127.0.0.1:8000/squares/](http://127.0.0.1:8000/squares/) where we should see the number 4 appear on our screen.

## What is a request?

> In Django, a request represents an HTTP request made by a client (e.g., a web browser) to the Django server. The request contains information such as the URL, HTTP method (e.g., GET, POST), headers, and any submitted data.

> When a request is received by the Django server, it is passed to the appropriate view function or class based on the URL pattern. The view then processes the request and returns an HTTP response, which is sent back to the client.

> Create a `circle_area_view` functional view that will take in a request and return the area of a circle with a radius of 2. Lets print `request` within this view and take a look at what our Django Server prints to our terminal every time a request is processed.

```python
# pokedex_proj/urls
import math

def circle_area_view(request):
    print(request)
    area_of_a_circle = math.pi * (2 ** 2)
    return HttpResponse(area_of_a_circle)
```

> In the example above, the `circle_area_view` function is responsible for handling requests to the `circles/` URL. It currently returns the `area` of a circle but a `view` could potentially return just about anything. Test is by traveling to [http://127.0.0.1:8000/circles/](http://127.0.0.1:8000/circles/). Look at the Django Terminal to see the output of our print statement and experiment with the following request headers:

- request.method = returns the requests method
- request.body = returns the body of the request within a binary string
- request.headers = returns almost all information about the origin of the request

> We don't expect you to understand these, we expect you to know they exist and familiarize yourself with these topics on your own time.

## How to pass parameters through URL patterns?

> URL patterns in Django can include parameters that are captured and passed to the corresponding view function or class. Parameters are specified within angle brackets `< >` in the URL pattern definition and by default can only be of type `integer(int)` or type `string(str)`.

```python
path('triangles/height/<int:height>/base/<int:base>/', triangle_area_view, name='triangle'),
```

> In the example above, the URL pattern `triangles/height/<int:height>/base/<int:base>/` captures integer parameters (`height` and `base`) and  and passes it to the `triangle_area_view` function.

```python
# pokedex_proj/urls

def triangle_area_view(request, height, base):
    print(f"Height: {height}\nBase: {base}")
    area_of_a_triangle = (height * base)/2
    return HttpResponse(area_of_a_triangle)
```

> The `triangle_area_view` function can access the captured parameters as arguments and use them to display the details of a specific triangles area. Lets test it with the following:

- [http://127.0.0.1:8000/triangles/height/5/base/4/](http://127.0.0.1:8000/triangles/height/5/base/4/)
- [http://127.0.0.1:8000/triangles/height/20/base/6/](http://127.0.0.1:8000/triangles/height/20/base/6/)
- [http://127.0.0.1:8000/triangles/height/2/base/30/](http://127.0.0.1:8000/triangles/height/2/base/30/)

## Conclusion

> The Django server is a crucial tool for local development and testing of Django applications. By using `python manage.py runserver`, you can start the development server and access your application through a local URL. Understanding the concepts of urlpatterns, paths, views, requests, and parameter passing allows you to define the URL structure, link it to appropriate views, process requests, and create dynamic and interactive web applications with Django.
