# myapp/urls.py

from django.urls import path
from .views import RegisterView, LoginView, home_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', home_view, name='home'),
]
