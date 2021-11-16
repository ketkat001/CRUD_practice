from django.test import TestCase
from .models import Article
from ..account.models import User
import json

# Create your tests here.


class CreateTest(TestCase):
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
    
    def test_create_article(self):
        data = {
            'title': 'test_title',
            'content': 'test_success',
            'user': self.user,
        }
        response= self.client.post('/community/', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)