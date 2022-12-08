from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Blogger(models.Model):
    userName = models.ForeignKey(User,max_length=20,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname

class BlogDetails(models.Model):
    title = models.CharField(max_length=50,blank=False)
    blogContent = models.TextField(blank=False)
    dateAdded = models.DateField(auto_now=True)
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE)
    blogger = models.ForeignKey(Blogger,on_delete=models.CASCADE)
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.title
