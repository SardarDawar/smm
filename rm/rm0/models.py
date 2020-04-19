from django.db import models

# Create your models here.

class contact(models.Model):
    Name           =       models.CharField(max_length=100)
    Email          =       models.CharField(max_length=100)
    Subject        =       models.CharField(max_length=100)
    Message        =       models.TextField()

    def __str__(self):
        return self.Name

class portfolio(models.Model):
    title           =     models.CharField(max_length=100)
    sub_title       =     models.CharField(max_length=100)
    image           =     models.ImageField()

    def __str__(self):
        return self.title
