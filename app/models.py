from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mess(models.Model):
    mess_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    cutprice = models.IntegerField()
    mapurl = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images")
    address = models.TextField(blank=True, null=True)
    dish1 = models.CharField(max_length=100, blank=True)
    dish2 = models.CharField(max_length=100, blank=True)
    dish3 = models.CharField(max_length=100, blank=True)
    dish4 = models.CharField(max_length=100, blank=True)
    dish5 = models.CharField(max_length=100, blank=True)
    dish6 = models.CharField(max_length=100, blank=True)
    dish7 = models.CharField(max_length=100, blank=True)

  
       
