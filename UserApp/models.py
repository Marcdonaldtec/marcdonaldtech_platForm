from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    first_name = models.CharField(max_length=150, default='')  # Add a default value here
=======
    first_name = models.CharField(max_length=150, default='') 
>>>>>>> 275d7765e9dd1b476bacfce6d6bfc918eb07bad2
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

