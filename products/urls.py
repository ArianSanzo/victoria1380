from django.urls import path
from . import views
from .views import ProductUpdateView


app_name = 'products'

urlpatterns = [
    path('', views.products_list, name="list"),
    path('update/<slug:slug>', ProductUpdateView.as_view(), name='update_page'),
]