from django.test import TestCase
from .models import *
from django.utils import timezone
import datetime
import signals

class PostTests(TestCase):
    def createpost(self):
        Post.objects.create(author=Author.objects.get(id=1))
        ps1 = Post.objects.get(id=1)
        ps1.postCategory.add(id=1)
        ps1.title = 'Title for first article'
        ps1.text = 'This text was written to fill the required field in article.'
        ps1.save()

        print(ps1.postCategory)
