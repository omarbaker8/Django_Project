from django.urls import path
from .views import (
    ViewProfile
)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile/<int:pk>/', ViewProfile.as_view(), name='profile-detail'),
]