from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate  
from django.contrib.auth import login as auth_login

# User register
def register(request):
    if (request.method == 'GET'):
        return render(request, 'register.html')
    
    elif (request.method == 'POST'):
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get ('password')
        email = request.POST.get('email')

        # Check if the name exists
        if User.objects.filter(username=username).exists():
            return HttpResponse(f"O usuário {username} já existe", status=409)
        
        # Create the user
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first,  
            last_name=last     
        )
        
        
        return redirect('users:login')
    
# User login
def login(request):

    if (request.method == 'GET'):
        return render(request, 'login.html')
    
    else:
        usernameLogin = request.POST.get('username')
        passwordLogin = request.POST.get('password')

        user = authenticate(username=usernameLogin, password=passwordLogin)

        if user:
            auth_login(request, user)
            return render (request, 'add_food.html', status=200)
        
        else:
            return HttpResponse('Usuário não encontrado', status = 404)

