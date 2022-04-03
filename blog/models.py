from urllib import request
from django.db import models

# Creating a subclass of models.Model
# Can use everything within django.db.models.Models
class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  body = models.TextField()

  def __str__(self):
    return self.title
