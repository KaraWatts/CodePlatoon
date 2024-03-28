from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class All_books(APIView):
    def get(self, request):
        books = Book.objects.all()

        ser_books = BookSerializer(books, many=True)

        return Response(ser_books.data)
    
class A_book(APIView):
    def get(self, request, id):
        book = Book.objects.get(id = id)
        ser_book = BookSerializer(book)
        return Response(ser_book.data)
    