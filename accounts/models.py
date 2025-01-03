from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Profile(User):
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField()
    stack = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    language = models.CharField(max_length=20)
    about_me = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name

class Project(models.Model):
    thumbnail = models.ImageField(upload_to='project/images', null=True, blank=True)
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    icon = models.FileField(upload_to='social_media/icons/', validators=[FileExtensionValidator(['svg'])])
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='socials')

    def __str__(self):
        return self.name

class ContactMe(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.full_name
