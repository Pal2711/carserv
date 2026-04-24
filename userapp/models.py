from django.db import models

# Create your models here.

class usersignup(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=25)
    
    def __str__(self):
        return self.username
    

class usercontact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name  = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class bookservice(models.Model):
    submited = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    phone = models.CharField(max_length=25)
    service = models.CharField(max_length=50)
    date = models.DateField()
    specialrequest = models.TextField()

    def __str__(self):
        return self.name
    
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='services/')  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

