from . import views
from django.urls import path

app_name = "product"


urlpatterns = [
    path('', views.index, name='home'),
    path('free-pictures/', views.pictures, name='pictures'),
    path('upload/', views.upload, name='upload'),
    path('free-pictures/edit/<int:pic_id>', views.edit, name='edit'),
    path('free-pictures/remove/<int:pic_id>', views.remove, name='remove')
]