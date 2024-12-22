from django.shortcuts import render,redirect
from . models import Order,OderedItem
from hai.models import producte
from django.contrib import messages


# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}    
    return render(request,'shoping-cart.html',context)
def remove_item_from_cart(request,id):
    remove_item=OderedItem.objects.get(id=id)
    if remove_item:
       remove_item.delete()
       return redirect('cart') 
    
        
def add_to_card(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        Product=producte.objects.get(id=product_id)
        

        orderd_item,created=OderedItem.objects.get_or_create(
            producte=Product,
            owner=cart_obj
            
            
            
            
        )
        if created:
            orderd_item.quantity=quantity
            orderd_item.save()
        else:
            orderd_item.quantity=+quantity
            orderd_item.save()    
        
                
    return redirect('cart')  

def checkout_cart(request):
  
    if request.POST:
        try:   
         user=request.user
         customer=user.customer_profile
         total=float(request.POST.get('total'))
         cart_obj=Order.objects.get(
             owner=customer,
             order_status=Order.CART_STAGE
         )
         if cart_obj:
             cart_obj.order_status=Order.ORDER_CONFIRMED
             cart_obj.save()
             status_massage='your order is processed. Your item will be delivered with in 2 days'
             messages.success(request,status_massage)       
         else:
             status_massage='unabel to processed. No items in cart'
             messages.error(request,status_massage)
        except Exception  as e:
            status_massage='unabel to processed. No items in cart'
            messages.error(request,status_massage)
    return redirect('cart')   
    