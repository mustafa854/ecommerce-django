from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    slug = models.SlugField()
    featuredImage = models.ForeignKey('ProductImage', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products')
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    
class Cart(models.Model):
    PAYMENT_STATUS = [
        ("P", "PENDING"),
        ("C", "COMPLETED"),
        ("R", "REFUNDED"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid = models.CharField(max_length=2, choices=PAYMENT_STATUS, default="P")
    total_bill = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)    
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.title
    
    
class Address(models.Model):
    street_address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pin_code = models.IntegerField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=6,decimal_places=2)
    email = models.EmailField()
    payment_id = models.CharField(max_length=255)
    payer_id = models.CharField(max_length=255)

class Orderitems(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

