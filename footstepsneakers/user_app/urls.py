from django.contrib.auth.views import LoginView, LogoutView

from . import views
from django.urls import path

from .forms import LoginForm

app_name = "user_app"

urlpatterns = [
    path('', views.RegisterView.as_view(), name='register'),
    path('signin/',
         LoginView.as_view(template_name='user_app/login.html', form_class=LoginForm, redirect_authenticated_user=True),
         name='signin'),
    path('logout/', LogoutView.as_view(template_name='user_app/logout.html'), name='logout'),
]