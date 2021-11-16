from django.test import TestCase, Client
from .models import User

import json
# Create your tests here.

client = Client()

class SignupTest(TestCase):
    def test_signup(self):
        data = {
            'password': '1q2w3e4r!!',
            'username': 'ketkat',
            'first_name': 'YONGJOON',
            'last_name': 'KANG',
            'email': 'ketkat001@naver.com',
        }
        response = client.post('/account/signup/', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)