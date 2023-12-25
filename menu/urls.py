from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('index/produk/', views.produk, name='produk'),
    path('produk/details/<int:id>', views.detail_produk, name='detailproduk'),
    path('index/aku/', views.aku, name='aku'),
    path('index/', views.index, name='index'),
    path('index/contact/', views.contact, name='contact'),

]