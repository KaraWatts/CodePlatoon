from django.db import models
from .validators import validate_title_case, validate_isbn

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, validators=[validate_title_case])
    author = models.CharField(max_length=50, validators=[validate_title_case])
    isbn = models.CharField(max_length=14, unique=True, validators=[validate_isbn])
    genre = models.CharField(max_length=50, validators=[validate_title_case])
    published_date = models.DateField()
    