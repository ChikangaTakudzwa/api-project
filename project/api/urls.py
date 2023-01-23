from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books , name="books")
    path('books/<int:book_id>', views.books)
]