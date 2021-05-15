from django.db import models
from django.contrib.auth.models import User

CATEGORIES = [
    ("Actualités", "Actualités"),
    ("Prgrammation", "Programmation")
]

STATUS = [
    (0, "Brouillon"),
    (1, "Publier")
]

class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    categorie = models.CharField(choices=CATEGORIES, default="Actualités", max_length=250)
    image = models.ImageField(upload_to="images/posts/", blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField("Votre nom".upper(), max_length=100)
    email = models.CharField("Votre mail".upper(), max_length=100)
    content = models.TextField("Votre message".upper())
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
