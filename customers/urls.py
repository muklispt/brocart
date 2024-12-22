from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.login,name='login'),
    path('ragister/',views.ragister,name='ragister'),
    path('sign_out',views.sign_out,name='sign_out')
    
   
]