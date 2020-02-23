from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('dash/', views.dashboard, name='dashboard'),
    path('add_sku/', views.add_sku, name='add_sku'),
    path('inventory_changelog/', views.inventory_changelog, name='inventory_changelog'),
    path('sales_log/', views.sales_log, name='sales_log'),
    path('delete_sku/<str:sku>/', views.delete_sku, name='delete_sku'),
    path('confirm_delete_sku/<str:sku>/', views.confirm_delete_sku, name='confirm_delete_sku'),
    path('<str:sku>/', views.update_sku, name='update_sku'),
]