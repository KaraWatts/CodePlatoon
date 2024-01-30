# models has many different methods we will utilize when creating our Models
from django.db import models
from django.utils import timezone
# import built-in Django Validators
from django.core import validators as v
from .validators import validate_name, validate_type
from move_app.models import Move

# Create your models here.
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=200, blank=False, null=False, validators=[validate_name])
    # Adding both the min and vax value will ensure Pokemon could only go from levels 1-100
    level = models.IntegerField(default=1, validators=[v.MinValueValidator(1), v.MaxValueValidator(100)])
    # Under the hood DateField is already running a regex function to ensure 
    # input is matching the correct date format of "YYYY-MM-DD"
    date_encountered = models.DateField(default="2008-01-01")
    # Under the hood DateField is already running a regex function to ensure 
    # input is matching the correct date format of "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]"
    date_captured = models.DateTimeField(default=timezone.now)
    # We don't want a pokemon's description to either be too long or too short so
    # lets add both a Max and Min LengthValidators to our TextField to ensure
    # input meets our criteria
    description = models.TextField(default="Unknown", validators=[v.MinLengthValidator(7), v.MaxLengthValidator(150)])
    # Boolean field is already ensuring to only take in either True or False
    captured = models.BooleanField(default = False)
    moves = models.ManyToManyField(Move, related_name="pokemon")
    type = models.CharField(default="normal", validators=[validate_type])

    # DUNDER METHOD
    def __str__(self):
        return f"{self.name} {'has been captured' if self.captured else 'is yet to be caught'}"

    # RAISES POKEMON'S LEVEL
    def level_up(self):
        self.level += 1
        self.save()

    # Switches Pokemon's captured status from True to False and vise versa
    def change_caught_status(self):
        self.captured = not self.captured
        self.save()