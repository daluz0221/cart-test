
from django.urls import path

from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('response/', views.Response.as_view(), name='response'),
    path('confirmation/', views.Success.as_view(), name='success'),
]
