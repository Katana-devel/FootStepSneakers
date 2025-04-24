from django.contrib.auth import user_logged_in
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, reverse

from cartitem.models import CartItem

from product.models import Sneakers


@login_required
def cart_index(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.sneakers.price * item.quantity for item in items)
    return render(request, 'cartitem/cart.html', {'cart_items': items, 'total': total})


@login_required
def add_to_cart(request, sneakers_id):
        sneaker = Sneakers.objects.filter(pk=sneakers_id).first()
        if request.method == 'POST':
            if sneaker:
                quantity = int(request.POST.get('quantity', 1))
                CartItem.objects.create(
                    user=request.user,
                    sneakers=sneaker,
                    quantity=quantity
                )
                return redirect("cartitem:cart")
            else:
                return redirect("cartitem:cart")
        return render(request, 'cartitem/add_to_cart.html', context={"sneaker": sneaker})
