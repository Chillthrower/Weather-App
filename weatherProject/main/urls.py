from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
]