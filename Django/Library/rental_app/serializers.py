from rest_framework import serializers
from .models import Rental
from book_app.serializers import BookSerializer
from client_app.serializers import ClientSerializer

class RentalSerializer(serializers.ModelSerializer):
    book_details = BookSerializer()
    renter = ClientSerializer()
    
    class Meta:
        model = Rental
        fields = '__all__'

