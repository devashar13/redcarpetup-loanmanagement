
# from account.views import MyTokenObtainPairView
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login',UserLoginView.as_view() , name='login'),
    path('profile', UserProfileView.as_view(),name="profile"),
    path('register', UserRegistrationView.as_view(),name="register"),
    
]
