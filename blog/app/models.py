from django.db import models

# Create your models here.
class Contact_us(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    image=models.ImageField()

    def __str__(self):
        return self.title
    