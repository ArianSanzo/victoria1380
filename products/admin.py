from django.contrib import admin
from .models import Product, Category, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

# Register your models here.
admin.site.register(Category)
admin.site.register(Image)