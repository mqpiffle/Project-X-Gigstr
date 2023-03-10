from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup')
]
