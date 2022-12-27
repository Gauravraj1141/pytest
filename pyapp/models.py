from django.db import models

# Create your models here.


class User_Blog(models.Model):
    U_id = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Desc = models.CharField(max_length=2000)
    Date = models.DateField(auto_now_add=True)
    Author = models.CharField(max_length=50, default="Gaurav")
