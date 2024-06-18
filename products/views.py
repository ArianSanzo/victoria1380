from django.shortcuts import render
from .models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.all().order_by('date')
    return render(request, 'products/products_list.html', {'products': products})
