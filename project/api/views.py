from django.shortcuts import render
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SingleBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SingleCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer










# @csrf_exempt
# def books(request, book_id):
#     # if request if get, get all values of table objects and assign to books variable
#     if request.method == "GET":
#         books = Book.objects.all().values()
#         # assigned 'books' as key in the books_dict and assign values to it
#         books_dict = {
#             "books": list(books)
#         }
#         return JsonResponse(books_dict)
#     # else if request is post get form data and assign to respective variables
#     elif request.method == "POST":
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         price = request.POST.get('price')

#         # assign the variable data from the request to the db table columns
#         book = Book(id=book_id, title=title, author=author, price=price)
#         # try to save if integrity error is raise return jason response of missing firls error with 400 status
#         try:
#             book.save()
#         except IntegrityError:
#             return JsonResponse({'error':'true', 'message':'required field missing'}, status=400)

#         return JsonResponse(model_to_dict(books), status=201)


