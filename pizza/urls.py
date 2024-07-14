from django.urls import path
from . import views

urlpatterns = [
    path('' , views.HomeTemplateView.as_view(), name='home.view'),
    path('order/', views.Order , name='order.view' ),
    path('pizzas/', views.pizzas , name='pizzas.view' ),
    path('edit_order/<int:pk>', views.edit_order , name='edit_order.view' ),
]
