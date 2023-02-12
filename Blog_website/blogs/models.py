from django.db import models

# Create your models here.
# Blog post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc=models.TextField()

# contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    feedback = models.TextField()

