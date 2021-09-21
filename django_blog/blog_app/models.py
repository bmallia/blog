from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
