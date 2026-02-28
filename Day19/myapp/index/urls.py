from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    # Corrected view names
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Product module
    path('product/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),

    # Optional: productdata endpoint (you didn’t write a view earlier)
    path('productdata/', views.productdata, name='productdata'),
]