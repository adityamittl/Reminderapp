from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=False)
    email = models.EmailField()
    purchased = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'media/Profile pictures', default = 'Profile pictures/default.png')
    def __str__(self):
        return str(self.user)
    

class friend(models.Model):
    friend = models.ForeignKey(Profile, on_delete=models.CASCADE)