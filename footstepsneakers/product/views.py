from pathlib import Path

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, login_not_required
from django.conf import settings

from product.models import Sneakers

from product.models import Picture

from product.forms import PictureForm


def index(request):
    sneakers = Picture.objects.filter(sneakers__is_public=True)
    return render(request, 'product/index.html', {'sneakers': sneakers})


@login_required
def pictures(request):
    pics = Picture.objects.filter(user=request.user).all()
    return render(request, 'product/pictures.html', context={"pics": pics})


def upload(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        custom_brand = request.POST.get("custom_brand")

        if custom_brand:
            brand = custom_brand

        color = request.POST.get("color")
        custom_color = request.POST.get("custom_color")

        if custom_color:
            color = custom_color

        sneakers = Sneakers.objects.create(
            brand=brand,
            model=request.POST.get("model"),
            color=color,
            price=request.POST.get("price"),
            description=request.POST.get("description"),
            is_public=request.POST.get("is_public", False),
        )

        if request.FILES.get("path"):
            sneakers.image = request.FILES["path"]
            sneakers.save()

        return redirect('product:success')

    return render(request, 'product/upload.html')


@login_required
def edit(request, pic_id):
    if request.method == 'POST':
        desc = request.POST.get('description')
        price = request.POST.get('price')
        color = request.POST.get('color')
        model = request.POST.get('model')
        brand = request.POST.get('brand')
        picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
        if picture:
            picture.sneakers.description = desc
            picture.sneakers.price = price
            picture.sneakers.color = color
            picture.sneakers.model = model
            picture.sneakers.brand = brand
            picture.sneakers.save()
        return redirect(to="product:pictures")

    pic = Picture.objects.filter(pk=pic_id, user=request.user).first()
    return render(request, 'product/edit_desc.html', context={"pic": pic})


@login_required
def remove(request, pic_id):
    pic = Picture.objects.filter(pk=pic_id, user=request.user)
    file_path: Path = settings.MEDIA_ROOT / str(pic.first().path)
    if file_path.exists():
        file_path.unlink()
        pic.delete()
        print('Removed file')
    else:
        print('File ont removed')

    return redirect(to="product:pictures")


