from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView.as_view(), name="books"),
    path('books/<int:pk>', views.SingleBook.as_view(), name="singlebook")
]