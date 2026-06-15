from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from cartitem.models import CartItem
from product.models import Sneakers


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        items = CartItem.get_for_user(request.user)
        total = sum(item.total_price for item in items)
        return render(request, 'cartitem/cart.html', {'cart_items': items, 'total': total})


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, sneakers_id):
        sneaker = Sneakers.objects.filter(pk=sneakers_id).first()
        return render(request, 'cartitem/add_to_cart.html', context={"sneaker": sneaker})

    def post(self, request, sneakers_id):
        sneaker = Sneakers.objects.filter(pk=sneakers_id).first()
        if sneaker:
            quantity = int(request.POST.get('quantity', 1))
            CartItem.objects.create(
                user=request.user,
                sneakers=sneaker,
                quantity=quantity,
            )
        return redirect("cartitem:cart")
