from django.urls import path

from cartitem import views

app_name = "cartitem"


urlpatterns = [
    path('confirm_add/<int:sneakers_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_index, name='cart')
]