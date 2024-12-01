from django.db import models  
from django.contrib.auth.models import User  

# Profile model extending the User model  
class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.png')  

    def __str__(self):  
        return f'{self.user.username} Profile'  