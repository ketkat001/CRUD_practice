from django.test import TestCase
from .models import Article
from account.models import User
import json

# Create your tests here.


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user", 
            password="1q2w3e4r!!",
            email="test@naver.com",
            first_name="test",
            last_name="user")
        self.user.save()
        self.article = Article.objects.create(
            title="test_title",
            content="test_content",
            user=self.user
        )
        self.article.save()


    def tearDown(self):
        self.user.delete()
        self.article.delete()
    

    def test_create_article(self):
        data = {
            'title': 'test_title',
            'content': 'test_success',
            'user': self.user.id,
        }
        response = self.client.post(
            '/community/', 
            json.dumps(data), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 200)


    def test_read_article_list(self):
        response = self.client.get('/community/')
        self.assertEqual(response.status_code, 200)
    

    def test_read_article_detail(self):
        response = self.client.get('/community/1/')
        self.assertEqual(response.status_code, 200)


    def test_update_article(self):
        change_title = {'title': 'changed_test_title'}
        response = self.client.put(
            '/community/1/', 
            change_title, 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 200)

    
    def test_delete_article(self):
        response = self.client.delete(
            '/community/1/',
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)