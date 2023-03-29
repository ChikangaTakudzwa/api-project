from django.contrib import admin
from api.models import Book, Category

# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ("title", "author", "price", "date")


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("slug", "name")