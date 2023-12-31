from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('index/pondok/', views.pondok, name='pondok'),
    path('pondok/details/<int:id>', views.detail_pondok, name='detailpondok'),
    path('index/aku/', views.aku, name='aku'),
    path('index/', views.index, name='index'),
    path('index/program/', views.program, name='program'),
    path('index/form/', views.form, name='form'),
    path('index/home/', views.home, name='home'),
]