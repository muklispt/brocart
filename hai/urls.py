from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('list',views.list_producte,name='list_pro'),
    path('delail/<int:id>',views.detail_product,name='detail'),
    
    
    
   
]