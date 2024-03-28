from django.urls import path
from .views import Rentals

urlpatterns = [
    path('', Rentals.as_view(), name="rentals"),
    # path('<int:rental_id>/', Rental_Details.as_view(), name="rentals"),
]