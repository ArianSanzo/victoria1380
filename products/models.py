from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify

# Create your models here.

class PrimaryCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class SecondaryCategory(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Size(models.Model):
    size = models.IntegerField()

    def __str__(self) -> str:
        return str(self.size)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField()
    primary_category = models.ForeignKey(PrimaryCategory, on_delete=models.PROTECT, related_name='products')
    secondary_categories = models.ManyToManyField(SecondaryCategory, related_name='products')
    sizes = models.ManyToManyField(Size, related_name='products')
    unique_size = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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