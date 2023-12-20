from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/', views.product, name = 'products'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login_user, name = 'login_user'),
    path('register/', views.register, name = 'register'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    path('create_customer/', views.create_customer, name = 'create_customer'),
    path('customer/<str:id>/', views.customer, name = 'customer'),
    path('create_order/<int:id>/', views.create_order, name = 'create_order'),
    path('update_order/<str:id>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:id>/', views.delete_order, name = 'delete_order'),
]