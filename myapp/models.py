from django.db import models

# Create your models here.
class person(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)


class person1(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
    image=models.ImageField()
    age=models.IntegerField()
    
    def __str__(self):
        return self.username
        
class datas(models.Model):
    name=models.CharField(max_length=16)
    price=models.CharField(max_length=12)
    category=models.CharField(max_length=20)
    size=models.CharField(max_length=10)
    image=models.ImageField()
    description=models.CharField(max_length=30)


class datarow(models.Model):
    name=models.CharField(max_length=16)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    size=models.IntegerField()
    image=models.ImageField()
    description=models.CharField(max_length=30)


class Userper(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=12)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)


class cart(models.Model):
    username=models.CharField(max_length=30)
    keyss=models.IntegerField()
    