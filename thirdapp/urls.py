from django.urls import path
from . import views

urlpatterns = [
   ### http://127.0.0.1:8000/third/
    path('', views.index),
    path('index/', views.index),

    ### http://127.0.0.1:8000/third/cart_list/
    path('cart_list/', views.getCartList),

    ### http://127.0.0.1:8000/third/cart_list/
    path('test/', views.getTest),

    ### http://127.0.0.1:8000/third/include_view/
    path('include_view/', views.include_view),



]