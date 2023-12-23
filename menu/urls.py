from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('produk/details/<int:id>', views.detail_produk, name='detailproduk'),
    path('aku/', views.aku, name='aku'),
    path('index/', views.index, name='index'),
    
]