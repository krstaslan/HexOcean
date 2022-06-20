from tkinter import CASCADE
from django.db import models
from PIL import Image as im
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class Size (models.Model): 
    thumbnail= models.IntegerField(null=True)   
    def __str__(self):
        return str(self.thumbnail)
    

class Tier(models.Model):
    name=models.CharField(max_length=200,null=True)
    thumbnails=models.ManyToManyField(
        Size, related_name='thumbnails', blank=True)
    access_original=models.BooleanField(default=False)
    ability_expire=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(models.Model):
    name=models.CharField(max_length=200,null=True)
    tier=models.ForeignKey(Tier,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Image(models.Model):
    image=models.ImageField(upload_to='static/images/')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="images")
    expireTime=models.IntegerField(null=True,blank=True,default=0,
            validators=[
            MaxValueValidator(30000),
            MinValueValidator(300)
        ]
        )
    created_time = models.DateTimeField(auto_now_add=True)
    def save(self,*args, **kwargs):
        super().save()
        img = im.open(self.image.path)
        if not img.format=="PNG" or img.format=="JPG":
            raise ValidationError("Only .jpg and .png image accepted")
        super(Image,self).save(*args, **kwargs)