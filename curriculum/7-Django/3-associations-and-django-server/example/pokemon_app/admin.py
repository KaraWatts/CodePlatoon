# Pokemon_app/admin.py
from django.contrib import admin
# Explecit import of Pokemon Model
from .models import Pokemon

# Register your models here.
admin.site.register([Pokemon])