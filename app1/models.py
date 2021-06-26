from django.db import models

# Create your models here.
class seller(models.Model):
    fname = models.CharField(max_length=255,default="firstname")
    lname = models.CharField(max_length=255,default="lasttname")
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=255,default="password")