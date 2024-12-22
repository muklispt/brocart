from django.shortcuts import render,redirect
from . models import customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages


# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('/')

def ragister(request):


    if request.POST and 'ragister' in request.POST:
        


     try:
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        address=request.POST.get('addras')
        email=request.POST.get('email')
        # creates user accuonts 
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        ) 
        # creates customer accound 
        Customer = customer.objects.create(
            name=username,
            user=user,
            phone=phone,
            address=address
        )
        return redirect('login')
     except Exception as e:   

        error_message='Duplicate username or invalid credention'
        messages.error(request,error_message)    
    return render(request,'ragister.html')
       
    
def login(request):
    
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
           
           auth_login(request,user)  
           return redirect('/')
        else:
           error_message='Invalid username and password'
           messages.error(request,error_message)   
          
       
          

    
        

    return render(request,'login.html')