from django.urls import path
from . import views

urlpatterns = [
    path('', views.payments, name='payment'),
    path('success/', views.payment_success, name='payment_succcess'),
    path('failed/', views.payment_failed, name='payment_failed'),
]