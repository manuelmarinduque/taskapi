from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CreateUserAPIView, UserDetailsAPIView


urlpatterns = [
    path("register", CreateUserAPIView.as_view(), name="creation"),
    path("details", UserDetailsAPIView.as_view(), name="details"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
