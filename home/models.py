from django.db import models



# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    query = models.CharField(max_length=200) 
    def __str__(self):
        return self.email

class Info(models.Model):
    email = models.CharField( max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.email 