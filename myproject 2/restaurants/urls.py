from django.urls import path
from . import views

urlpatterns = [ path('', views.home,name='home'), 
    path('menu/', views.menu, name='menu'), 
    path('orders/', views.view_cart, name='orders'), 
    path('location/', views.location, name='location'), 
    path('contact/', views.contact, name='contact'), 
    path('add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('login/', views.login_user, name='login_user'), 
    path('logout/', views.logout_user, name='logout_user'), 
    ]