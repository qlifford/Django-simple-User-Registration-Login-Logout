from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/', views.product, name = 'products'),
    path('customer/<str:id>/', views.customer, name = 'customer'),
    path('create_order/<int:id>/', views.create_order, name = 'create_order'),
    path('update_order/<str:id>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:id>/', views.delete_order, name = 'delete_order'),
]