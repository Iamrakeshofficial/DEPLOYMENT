from django.test import TestCase
from .models import Blog
from django.contrib.auth.models import User
# Create your tests here.

class TestModel(TestCase):
    def test_post_model(self):
        title = Blog.objects.create(title='Food Blogs')
        description= Blog.objects.create(description='this is a wonderful Item andd taste is Very Good.')
        self.assertEqual(str(title), 'Food Blogs')
