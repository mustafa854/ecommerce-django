import paypalrestsdk
from django.conf import settings
from django.urls import reverse

from decimal import Decimal
from django.shortcuts import render, redirect
from requests import delete
from .models import Cart, Customer, Order, Orderitems, Product, CartItem
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    products = Product.objects.all()    
    return render(request, 'core/index.html', {
        'products':products
    })


def checkout(request):
    return render(request, 'core/checkout.html')


@login_required(login_url='/auth/login/')
def cart(request):
    try:
        cart = Cart.objects.get(user=request.user,paid="P")
        cartitems = CartItem.objects.filter(cart=cart)
        if cartitems:    
            print(cartitems)  
            return render(request, 'core/cart.html',{'cartitems':cartitems, 'cart':cart})
        else:
            messages.info(request,'No items in cart Exists, please add something to cart to proceed to checkout!')
            return render(request, 'core/cart.html')
    except Cart.DoesNotExist:
        messages.info(request,'No items in cart Exists, please add something to cart to proceed to checkout!')
        return render(request, 'core/cart.html')
    
    

def product(request, slug):
    try:
        product = Product.objects.get(slug=slug)  
        return render(request, 'core/product.html', {
        'product':product
    })
    except Product.DoesNotExist:
        return HttpResponse("404! Page not found!")
    
@login_required(login_url='/auth/login/')
def addToCart(request, slug):
    if request.method == 'POST':
        product_cart_quantity = int(request.POST.get('product_cart_quantity')) 
    else:
        product_cart_quantity = 1
    user = request.user
    try:
        product = Product.objects.get(slug=slug)
        print(product)
        try:
            cart_exists = Cart.objects.get(user=user,paid="P")
            try:
                cartItem_exists = CartItem.objects.get(cart__user=user,product=product)
                cartItem_exists.quantity = cartItem_exists.quantity + product_cart_quantity
                cartItem_exists.total_price = product.price*cartItem_exists.quantity
                cartItem_exists.save()
                print(cart_exists.total_bill)
                cart_exists.total_bill = Decimal(cart_exists.total_bill) + Decimal(product.price*product_cart_quantity)
                cart_exists.save()
            except CartItem.DoesNotExist:
                cartitem_netpay = product.price*product_cart_quantity
                print(cartitem_netpay)
                cartitem = CartItem.objects.create(product=product,quantity=product_cart_quantity,total_price=cartitem_netpay,cart=cart_exists)
                print(cart_exists.total_bill)
                cart_exists.total_bill = Decimal(cart_exists.total_bill) + Decimal(product.price*product_cart_quantity)
                cart_exists.save()
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user,total_bill=0)
            cartitem_netpay = product.price*product_cart_quantity
            cartitem = CartItem.objects.create(product=product,quantity=product_cart_quantity,total_price=cartitem_netpay,cart=cart)
            cart.save()
            print(cart.total_bill)
            cart.total_bill = Decimal(cart.total_bill) + Decimal(product.price*product_cart_quantity)
            cart.save()
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    except Product.DoesNotExist:
        return HttpResponse("Product can't be added to cart! Sorry!")

    
@login_required(login_url='/auth/login/')
def deleteFromCart(request, slug):
    user = request.user
    try:
        product = Product.objects.get(slug=slug)
        print(product)
        try:
            cart_exists = Cart.objects.get(user=user, paid="P")
            try:
                cartItem_exists = CartItem.objects.get(cart__user=user,product=product)
                cart_exists.total_bill = cart_exists.total_bill - cartItem_exists.total_price
                cart_exists.save()
                cartItem_exists.delete()
            except CartItem.DoesNotExist:
                 return HttpResponse('Please add the product to cart before deleting')
        except Cart.DoesNotExist:
            return HttpResponse('Please add some product to cart before deleting')
            
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    
    except Product.DoesNotExist:
        return HttpResponse("Product is out of stock or does not exists! Sorry!")


        

#PAYPAL INTEGRATION

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET,
})

def create_payment(request):
    cart = Cart.objects.get(user=request.user, paid="P")
    total_payment_amount = cart.total_bill
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
        "transactions": [
            {
                "amount": {
                    "total": str(total_payment_amount),  # Total amount in USD
                    "currency": "USD",
                },
                "description": "Payment for Product/Service",
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'paypal/payment_failed.html')
    
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            customer = Customer.objects.create(user=request.user)
        cart = Cart.objects.get(user=request.user, paid="P")
        payment_id = request.GET.get('paymentId')
        payer_id = request.GET.get('PayerID')
        order = Order.objects.create(customer=customer, cart=cart, total_payment=cart.total_bill, email=request.user.email, payment_id=payment_id,payer_id=payer_id)
        cartItems = cart.cartitem_set.all()
        for cartItem in cartItems:
            Orderitems.objects.create(products=Product.objects.get(title=cartItem), quantity=cartItem.quantity, total_price = cartItem.total_price, order=order)
        cartItems.delete()    
        cart.paid = "C"   
        cart.save()
        return render(request, 'paypal/payment_success.html')
    else:
        return render(request, 'paypal/payment_failed.html')

# def payment_checkout(request):
#     return render(request, 'checkout.html')


def payment_failed(request):
    return render(request, 'paypal/payment_failed.html')



def demo(request):
    carts = Cart.objects.get(user=request.user, paid="P").cartitem_set.all() 
    for cart in carts:
    # Access dynamic values for each cart item within the loop
        product = cart  # Access the product related to the cart
        quantity = cart.quantity
        total_price = cart.total_price
        print(cart)
        print(product)
        print(quantity)
        print(total_price)
        print("--------------")
        
        # Create OrderItem instances with dynamic values
        #Orderitems.objects.create(products=product, quantity=quantity, total_price=total_price, order=order)
# Once all OrderItems are created, delete cart items
    # cart.cartitem_set.all().delete()

    # return render(request, 'paypal/payment_success.html')
    return HttpResponse('hi')