from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	bio = models.CharField(max_length=150)
	profile_picture = models.ImageField()
	followers = models.ManyToManyField("self", symmetrical=False, related_name="following")