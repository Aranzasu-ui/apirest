from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from library.models import Books
from library.serializers import BooksSerializer

@api_view(['GET', 'POST'])
def book_list(request): #será la utilizada para devolver todos los libros en la biblioteca o para insertar un nuevo libro.
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        books = Books.objects.all() # el cual devolverá una lista de instancias de la clase Book
        serializer = BooksSerializer(books, many=True) #le pasara en el constructor los datos enviados en la petición (request.data).
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

