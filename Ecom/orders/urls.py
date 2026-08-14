from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:id>/', views.order_details, name='order_details'),
    path('checkout/', views.checkout, name='checkout'),
]