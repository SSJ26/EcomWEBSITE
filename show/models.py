from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

# class Role(models.Model):
#     CUSTOMER=1
#     SELLER=2
#     ADMIN=3
    
#     id=models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#     def __str__(self):
#         return self.get_id_display()
ROLE_CHOICES=(
        ('CUSTOMER','customer'),
        ('SELLER','seller'),
        ('ADMIN','admin'),
    )
class StoreUser(AbstractUser):
    roles=models.CharField(choices=ROLE_CHOICES,blank=True,null=True,max_length=10)
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    



class Product(models.Model):
    name=models.CharField(max_length=20,unique=True)
    desc=models.CharField(max_length=40)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_by=models.ForeignKey(StoreUser,on_delete=models.CASCADE,null=True,blank=True)
    likes=models.IntegerField(default=0)
    img=models.ImageField(upload_to='images')
    amount = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    phone=models.IntegerField()
    concern=models.TextField(max_length=200)
    

class Buy(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.PROTECT)
    user_id = models.ForeignKey(StoreUser,on_delete=models.CASCADE, related_name='customer_id')
    time = models.DateField(auto_now_add=True)
    # seller id 
    seller_id=models.ForeignKey(StoreUser, on_delete=models.CASCADE, related_name='seller_id')
    # amount
    


class Cart(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.PROTECT)
    user_id = models.ForeignKey(StoreUser,on_delete=models.CASCADE)
    time = models.DateField(auto_now_add=True)

    
