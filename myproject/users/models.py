from django.db import models

# Create your models here.

class User(models.Model):
  # title = models.CharField(max_length=75)
  # body = models.TextField()
  # slug = models.SlugField()
  # date = models.DateTimeField(auto_now_add=True)
  # #Need to import Pillow for imagefield
  # banner = models.ImageField(default='fallback.png', blank=True)

  username = models.CharField(max_length=25)
  password = models.CharField(max_length=25)

  def __str__(self):
    return self.username