from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    #path('checkout/', views.checkout, name='checkout'),
    path('demo/demo', views.demo),
    
    #paypal route
    path('create_payment/', views.create_payment, name='create_payment'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    
    path('<slug>/', views.product, name='product'),
    path('add-to-cart/<slug>', views.addToCart, name='add_to_cart'),
    path('delete-from-cart/<slug>', views.deleteFromCart, name='delete_from_cart'),
    
]
