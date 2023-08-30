from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import User
from rest_framework_simplejwt.tokens import RefreshToken

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
            "first_name": "string",
            "last_name": "string",
        }
        response = self.client.post(reverse("register"), user_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

