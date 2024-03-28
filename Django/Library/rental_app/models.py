from django.db import models
from book_app.models import Book
from client_app.models import Client
from datetime import timedelta
from django.utils import timezone


# Create your models here.
class Rental(models.Model):
    book_details = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='rental_details')
    renter = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='rentals')
    date_rented = models.DateField()
    due_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set default value if the object is being created for the first time
            self.date_rented = timezone.now().date()
            self.due_date = self.date_rented + timedelta(weeks=2)
        super().save(*args, **kwargs)