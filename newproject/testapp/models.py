from django.db import models

# Create your models here.
class Login(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    em=models.EmailField()
    passw=models.CharField(max_length=30)
    repassw=models.CharField(max_length=30)
