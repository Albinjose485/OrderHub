from django.db import models
from django.contrib.auth.models import User



class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image= models.ImageField(upload_to='media/product_image/',null=True,blank=True)
    description=models.CharField(max_length=40,default='plz,enter')

    def __str__(self):
        return self.name
    

class CartItem(models.Model):
    Dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'