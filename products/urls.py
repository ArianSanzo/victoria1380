from django.urls import path
from . import views
from .views import ProductUpdateView, ProductCreateView, ProductListView


app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="list"),
    path('update/<slug:slug>', ProductUpdateView.as_view(), name='update_page'),
    path('create-product/', ProductCreateView.as_view(), name='create_page'),
]