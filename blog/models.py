from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class post(models.Model):

    title=models.CharField(max_length=100)
    category=models.CharField(max_length=200)
    header_image = models.ImageField(upload_to='image/', blank=True, null=True)
    auth=models.ForeignKey(User, related_name=('post'), on_delete=models.CASCADE)
    body=RichTextField(null=True, blank=True)
    post_date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User, related_name='blog_posts')
    snippet=models.CharField(max_length=200 ,default='click above link...')
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("home")
                       
    

class comment(models.Model):
    post=models.ForeignKey(post, related_name="comment", on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    body=models.TextField(max_length=400)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s: %s' % (self.name, self.post)


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("home")

class profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField(max_length=255 ,null=True, blank=True)
    prof_image = models.ImageField(null=True  ,blank=True, upload_to='images/profile')
    

    def __str__(self):
        return self.user.username
    
