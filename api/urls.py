from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from api.views import UserCreateAPIView, UserListAPIView



urlpatterns = [
    path("api/v1/usercreate/", UserCreateAPIView.as_view(), name="register"),
    path("api/v1/users/", UserListAPIView.as_view(), name="list"),
    path(
        "api/login/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair_after_login",
    ),
]