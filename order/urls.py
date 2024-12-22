from django.urls import path
from . import views
urlpatterns=[

  path('cart',views.show_cart,name='cart'),
  path('add_cart',views.add_to_card,name="add_cart"),
  path('item_remove/<int:id>',views.remove_item_from_cart,name='item_remove'),
  path('checkout_cart',views.checkout_cart,name='checkout_cart')
    
   
]