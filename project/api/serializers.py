from .models import Book, Category
from rest_framework import serializers
from decimal import Decimal
from django.utils.dateparse import parse_date


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id', 'slug', 'name']

class BookSerializer(serializers.ModelSerializer):
    muridzi = serializers.CharField(source='author')
    # code to link the price_after_tax method to the serializer
    after_tax = serializers.SerializerMethodField(method_name= 'price_after_tax')
    date = serializers.DateTimeField(format='%Y-%m-%d')
    # category = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ['id', 'title', 'muridzi' , 'price', 'after_tax', 'date']

    # method to calculate tax of and return total price with 10 % tax
    def price_after_tax(self, product:Book):
        with_tax = product.price * Decimal(1.1)
        return round(with_tax, 2)