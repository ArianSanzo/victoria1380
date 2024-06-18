from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
     path('login-hidden/', views.login_view, name="login"),
     path('logout/', views.logout_view, name="logout"),
]