from django.db import models
from django.utils import timezone

# Create your models here.
# models.Model tell Django this is a Model that should be reflected on our database
class Pokemon(models.Model):
    # CharField is a character field and has a default max length of 255 characters
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    # IntegerField will allow only solid numerical values as input
    level = models.IntegerField(default=1)
    # We are providing a default to someone born Jan 1st 2008
    date_encountered = models.DateField(default="2008-01-01")
    # If a value is not provided we are stating the last time this pokemon was at school was upon creation of the classes instance.
    date_captured = models.DateTimeField(default=timezone.now)
    # If no value is provided the Pokemon description will be "Unknown"
    description = models.TextField(default="Unknown")
    # We must catch them all.
    captured = models.BooleanField(default = False)

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