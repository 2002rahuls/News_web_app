from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from email.message import Message
from django.db import models
from django.forms import EmailField

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()