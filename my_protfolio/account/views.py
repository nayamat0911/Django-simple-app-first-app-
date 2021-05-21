from django.shortcuts import render, redirect
from django.contrib.auth import authenticate ,login,  logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def user_log(request):
        if request.method == 'POST':
                username =request.POST['userame']
                password =request.POST['password']
                user = authenticate(request,username = username, password = password)
                if user is not None:
                        login(request,user)
                        return redirect('home')
                else:
                        messages.error(request, 'Email or  password invalid!', extra_tags='alert')
                    
        
        return render(request, './auth/login.html',{})
def sign_up(request):
        if request.method =="POST":
                name=request.POST('name')
                email =request.POST('email')
                password=request.POST('password')
                confrom_password=request.POST('confrom_password')
                if password==confrom_password:
                        return
                else:
                        messages.error(request, 'Password and Confrom Passwoed not matched!', extra_tags='alert')



        return render(request, './auth/sign_up.html',{})
def forgot_pasword(request):
        return render(request, './auth/forgot_pasword.html',{})

def user_logout(request):
        logout(request)
        messages.success(request, 'Your successfully logout!!', extra_tags='alert')
        return redirect('login')
    










#     if request.method == 'POST':
#                 name = request.POST('name')
#                 email = request.POST('email')
#                 password = request.POST('password')
#                 confrom_password = request.POST('confrom_password')
#                 if password == confrom_password:
#                         if User.objects.filter(username=name).exists():

#                                 messages.error(request, 'Username Allready Exist!', extra_tags='alert')
#                         elif User.objects.filter(email=email).exists():
#                                 messages.error(request, 'Email Allready Exist!', extra_tags='alert')
#                         else:
#                                 user = User.objects.create_user(username=name,password=password,email=email)
#                                 user.save()
#                                 return redirect('login')
                    
#                 else:
#                         messages.error(request, 'Password and Confrom Passwoed not matched!', extra_tags='alert')