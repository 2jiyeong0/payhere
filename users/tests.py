from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User

class SignupViewAPIViewTestCase(APITestCase):
    # 회원가입 성공
    def test_signup_success(self):
        url = reverse("user_view")
        user_data = {
        "email":"test@test.com",
        "password":"password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)
    
    # 회원가입 실패(이메일 중복)
    def test_signup_email_unique_fail(self):
        User.objects.create_user("test@test.com", "password")
        url = reverse("user_view")
        user_data = {
            "email": "test@test.com",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
    
    # 회원가입 실패(이메일 빈칸)
    def test_signup_email_blank_fail(self):
        User.objects.create_user("test@test.com", "password")
        url = reverse("user_view")
        user_data = {
            "email": "",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)

    # 회원가입 실패(이메일 형식)
    def test_signup_email_invalid_fail(self):
        User.objects.create_user("test@test.com", "password")
        url = reverse("user_view")
        user_data = {
            "email": "test",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 400)
