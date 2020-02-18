from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('dash/', views.dashboard, name='dashboard'),
    path('add_sku/', views.add_sku, name='add_sku'),
    path('<str:sku>/', views.update_sku, name='update_sku'),

]