from django.test import TestCase
from .models import User

import json
# Create your tests here.


class SignupTest(TestCase):
    def test_signup(self):
        data = {
            'password': '1q2w3e4r!!',
            'username': 'ketkat',
            'first_name': 'YONGJOON',
            'last_name': 'KANG',
            'email': 'ketkat001@naver.com',
        }
        response = self.client.post('/account/signup/', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", 
            password="1q2w3e4r!!",
            email="test@naver.com",
            first_name="test",
            last_name="user")
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_login(self):
        data = {
            'password': '1q2w3e4r!!',
            'username': 'test_user',
        }
        response= self.client.post('/account/login/', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)