from distutils.command.upload import upload
from multiprocessing import Value
from random import choice, choices
from tkinter import CASCADE
import django
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField

class Database(models.Model):
    video_backgraound_image =models.ImageField(default='default.jpg ', null=True, upload_to='video_photoes')
    video = models.FileField(upload_to='videos_uploaded',null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=django.utils.timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    release_date =models.DateTimeField(auto_now_add=True, null=True, editable=True)
    main_actors = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=30)
    movie_poster = models.CharField(max_length=100)
    movie_trailer_link= EmbedVideoField()

    def __str__(self):
        return str(self.title)
    class Meta:
        ordering = ["-date_uploaded"]
 

class Profile(models.Model):
    choice=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ]
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    gender=models.CharField(max_length=10, choices=choice)
    age=models.PositiveIntegerField(default=0)
    profile_image =models.ImageField(default='default.jpg ', null=True, upload_to='photoes')
    registration_date=models.DateTimeField(default=django.utils.timezone.now)


def __str__(self):
    return 'Profile for user {}'.format(self.user.username)

# Create your models here.
class contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    comment=models.TextField(max_length=300)

def __str__(self):
    return self.username  