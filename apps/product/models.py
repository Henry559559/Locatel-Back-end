from django.db import models
from datetime import datetime
from apps.category.models import Category

from django.conf import settings
domain = settings.DOMAIN

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/')
    descripcion = models.TextField()
    iva = models.CharField(max_length=2)
    number_iva = models.DecimalField(max_digits=6, decimal_places=2)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    compare_valor = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)

    def get_thumbnail(self):
        if self.photo:
            return self.photo.url
        return ''
    
    def __str__(self):
        return self.name