from django.urls import path

from . import views

app_name = "product"

urlpatterns = [
    path('', views.ProductIndexView.as_view(), name='home'),
    path('free-pictures/', views.PicturesView.as_view(), name='pictures'),
    path('upload/', views.UploadView.as_view(), name='upload'),
    path('free-pictures/edit/<int:pic_id>', views.EditView.as_view(), name='edit'),
    path('free-pictures/remove/<int:pic_id>', views.RemoveView.as_view(), name='remove'),
]