from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    gender=[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    gender_type=models.CharField(choices=gender,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
 



class PERSONMODEL(models.Model):
    gender=[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    gender_type=models.CharField(choices=gender,max_length=100,null=True)
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Media/person_image')
 
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):   
        
        return f"{self.name}"
    



    
  