from django.urls import path
from . import  views
urlpatterns = [
    path('', views.index,name="index"),
    path('add/', views.add,name="add"),
    path("addrec/", views.addrec,name="addrec"),
    path('delete/<int:id>/', views.delete,name="delete"),
    path('update/<int:id>/', views.update,name="update"),
    path('update/uprec/<int:id>/', views.uprec,name="uprec"),
    path('weapon/<int:id>/kurangi/', views.kurangi_stok, name='kurangi_stok'),
    path('weapon/<int:id>/tambah/', views.tambah_stok, name='tambah_stok'),
    path('riwayat_stok/', views.riwayat_stok, name='riwayat_stok')
]