from django.forms import BooleanField
from django.forms.fields import CharField, IntegerField, Textarea
from django.forms.models import ModelForm
from .models import Picture, Sneakers

class PictureForm(ModelForm):
    brand =CharField(max_length=30)
    model =CharField(max_length=30)
    color =CharField(max_length=30)
    price =IntegerField()
    description = CharField(max_length=300)
    is_public = BooleanField()

    class Meta:
        model = Picture
        fields = ['path']