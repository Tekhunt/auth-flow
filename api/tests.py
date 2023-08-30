from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import resolve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from api.views import UserCreateAPIView, UserListAPIView, UserRetrieveUpdateDestroyAPIView

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        self.user = User.objects.create_user(**self.user_data)
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Welcome to the auth flow")
        self.assertTrue(type(response.data["message"]), str)

    
    def test_user_create(self):
        user_payload = {
            "email": "user@example.com",
            "password": "string",
            "name": "string",
        }
        response = self.client.post(reverse("register"), user_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_users_url_is_resolved(self):
        url = reverse("register")
        self.assertEquals(resolve(url).func.view_class, UserCreateAPIView)

    def test_user_detail_url_is_resolved(self):
        url = reverse("single-user", args=[1])
        self.assertEquals(resolve(url).func.view_class, UserRetrieveUpdateDestroyAPIView)

    
    def test_userdata_list_url_is_resolved(self):
        url = reverse("list")
        self.assertEquals(resolve(url).func.view_class, UserListAPIView)

    def test_auth_token_url_is_resolved(self):
        url = reverse("token_obtain_pair_after_login")
        self.assertEquals(resolve(url).func.view_class, TokenObtainPairView)
