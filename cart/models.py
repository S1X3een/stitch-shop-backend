# cart/models.py
from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')  # Specify related_name
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')  # Specify related_name
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')  # Specify related_name
    quantity = models.IntegerField()
