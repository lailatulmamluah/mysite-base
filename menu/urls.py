from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('produk/', views.produk, name='produk'),
    path('aku/', views.aku, name='aku'),
    path('index/', views.index, name='index'),
    
]