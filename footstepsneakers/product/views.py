from pathlib import Path

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View

from product.models import Sneakers, Picture


class ProductIndexView(View):
    def get(self, request):
        sneakers = Picture.objects.filter(sneakers__is_public=True)
        return render(request, 'product/index.html', {'sneakers': sneakers})


class PicturesView(LoginRequiredMixin, View):
    def get(self, request):
        pics = Picture.get_for_user(request.user)
        return render(request, 'product/pictures.html', context={"pics": pics})


class UploadView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'product/upload.html')

    def post(self, request):
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
            is_public=request.POST.get("is_public") == "True",
        )

        image_file = request.FILES.get("path")
        if image_file:
            Picture.objects.create(
                user=request.user,
                path=image_file,
                sneakers=sneakers,
            )

        return redirect('product:pictures')


class EditView(LoginRequiredMixin, View):
    def get(self, request, pic_id):
        pic = Picture.objects.filter(pk=pic_id, user=request.user).first()
        return render(request, 'product/edit_desc.html', context={"pic": pic})

    def post(self, request, pic_id):
        picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
        if picture:
            picture.sneakers.description = request.POST.get('description') or picture.sneakers.description
            picture.sneakers.price = request.POST.get('price') or picture.sneakers.price
            picture.sneakers.color = request.POST.get('color') or picture.sneakers.color
            picture.sneakers.model = request.POST.get('model') or picture.sneakers.model
            picture.sneakers.brand = request.POST.get('brand') or picture.sneakers.brand
            picture.sneakers.save()
        return redirect(to="product:pictures")


class RemoveView(LoginRequiredMixin, View):
    def get(self, request, pic_id):
        pic = Picture.objects.filter(pk=pic_id, user=request.user)
        file_path: Path = settings.MEDIA_ROOT / str(pic.first().path)
        if file_path.exists():
            file_path.unlink()
        pic.delete()
        return redirect(to="product:pictures")


