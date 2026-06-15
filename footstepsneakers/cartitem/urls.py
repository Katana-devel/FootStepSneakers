from django.urls import path

from cartitem import views

app_name = "cartitem"

urlpatterns = [
    path('confirm_add/<int:sneakers_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('', views.CartView.as_view(), name='cart'),
]
