from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def square_area_view(request):
    area_of_a_square = 2 ** 2
    return HttpResponse(area_of_a_square)

def rectangle_perimeter(request, height, width):
    area_of_a_rectangle = height ** 2 + width ** 2
    return HttpResponse(area_of_a_rectangle)

def rectangle_area(request, height, width):
    area_of_a_rectangle = height ** width
    return HttpResponse(area_of_a_rectangle)