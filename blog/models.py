from django.db import models

# Create your models here.
class BlogFormModel(models.Model):
    author = models.CharField(max_length=100)
    program = models.TextField()
    screen = models.ImageField()
    function_name = models.CharField(max_length=100)

