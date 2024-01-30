"""
URL configuration for pokedex_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import math

def square_area_view(request):
    area_of_a_square = 2 ** 2
    return HttpResponse(area_of_a_square)

def circle_area_view(request):
    print(request.headers)
    area_of_a_circle = math.pi * (2 ** 2)
    return HttpResponse(area_of_a_circle)

def triangle_area_view(request, height, base):
    print(f"Height: {height}\nBase: {base}")
    area_of_a_triangle = (height * base)/2
    return HttpResponse(area_of_a_triangle)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('squares/', square_area_view, name='square'),
    path('circles/', circle_area_view, name='circle'),
    path('triangles/height/<int:height>/base/<int:base>/', triangle_area_view, name='triangle'),
    path("api/v1/pokemon/", include("pokemon_app.urls")),
    path('api/v1/moves/', include("move_app.urls")),
    path('api/v1/noun/', include("api_app.urls")),
]
