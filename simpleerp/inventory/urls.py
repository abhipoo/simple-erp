from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('dash/', views.dashboard, name='dashboard'),
]