from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Products(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,default='Dish')
    image=models.CharField(max_length=100,default='image.png')
    hotel=models.CharField(max_length=50,default='Hotel Name')
    price=models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)+" - "+self.name+" - "+self.image+" - "+self.hotel+" - "+str(self.price)

class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)],default=0)
    password=models.CharField(max_length=50)
    address=models.TextField(max_length=100)

    def __str__(self):
        return str(self.id)+" - "+self.name+" - "+str(self.phone)+" - "+self.password+" - "+self.address

class Orders(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,default='Dish')
    phone=models.IntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)],default=0)
    orders = models.TextField(max_length=1000)
    sum=models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.orders

class Total(models.Model):
    id = models.IntegerField(primary_key=True)
    earn=models.IntegerField(default=1)

    def __str__(self):
        return str(self.earn)