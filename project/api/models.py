from django.db import models
from django.db.models import DecimalField
import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        indexes = models.Index(fields=['price']),

    def __str__(self):
        return self.title