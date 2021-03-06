from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # www.meusite.com/blog/introducao-ao-django (esse é o slug, ele śo pode conter letra, 
    ##númemros hifen e underscore
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


    ##def get_absolute_url(self):
    ##    return reverse("blog:detail", kwargs:{"slug": self.slug})