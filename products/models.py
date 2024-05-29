from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField()
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = ProcessedImageField(upload_to='', 
                                processors=[ResizeToFill(800,600)], 
                                format='JPEG',
                                options={'quality': 80})
    def __str__(self) -> str:
        return f"Image from {self.product.name}"