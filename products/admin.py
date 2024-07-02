from django.contrib import admin
from .models import Product, PrimaryCategory, SecondaryCategory, Image, Size

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

# Register your models here.
admin.site.register(PrimaryCategory)
admin.site.register(SecondaryCategory)
admin.site.register(Size)
admin.site.register(Image)