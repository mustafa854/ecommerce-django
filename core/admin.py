from django.contrib import admin
from . import models



class ProductImageTabular(admin.TabularInline):
    model = models.ProductImage

class CartItemTabular(admin.TabularInline):
    model = models.CartItem

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular,]

#@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemTabular]

#@admin.register(models.CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

#@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

class OrderitemsTabular(admin.TabularInline):
    model = models.Orderitems

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderitemsTabular]

@admin.register(models.Orderitems)
class OrderitemsAdmin(admin.ModelAdmin):
    pass

@admin.register(models.profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

