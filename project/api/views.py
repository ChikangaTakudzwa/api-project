from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.


# @csrf_exempt
def books(request, book_id):
    # if request if get, get all values of table objects and assign to books variable
    if request.method == "GET":
        books = Book.objects.all().values()
        # assigned 'books' as key in the books_dict and assign values to it
        books_dict = {
            "books": list(books)
        }
        return JsonResponse(books_dict)
    # else if request is post get form data and assign to respective variables
    elif request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        # assign the variable data from the request to the db table columns
        book = Book(id=book_id, title=title, author=author, price=price)
        # try to save if integrity error is raise return jason response of missing firls error with 400 status
        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true', 'message':'required field missing'}, status=400)

        return JsonResponse(model_to_dict(books), status=201)


