from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout

#homefunction 
def home(request):
    return render(request, "home.html")

#registerfunction
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not first_name:
            messages.error(request, "Please fill in the first name.")
            return redirect('register')
        if not last_name:
            messages.error(request, "Please fill in the last name.")
            return redirect('register')
        if not username:
            messages.error(request, "Please fill in the username.")
            return redirect('register')
        if not email:
            messages.error(request, "Please fill in the email.")
            return redirect('register')
        if not password1:
            messages.error(request, "Please fill in the password.")
            return redirect('register')
        if not password2:
            messages.error(request, "Please fill in the confirm password.")
            return redirect('register')
        
        if password1 != password2:
            messages.info(request, "Passwords do not match.")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists.")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.save()
        messages.info(request, "User created successfully.")
        return redirect('login')

    return render(request, "register.html")
  


#loginfunction 
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username:
            messages.error(request, "Please fill in the username.")
            return redirect('login')
        
        if not password:
            messages.error(request, "Please fill in the password.")
            return redirect('login')
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    





    
#changeifnofunction    
def changeinfo(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        if not user.first_name:
            messages.error(request, "Please fill in the first name.")
            return redirect('register')
        if not user.last_name:
            messages.error(request, "Please fill in the last name.")
            return redirect('register')
        if not user.username:
            messages.error(request, "Please fill in the username.")
            return redirect('register')
        if not user.email:
            messages.error(request, "Please fill in the email.")
            return redirect('register')
        if (user.first_name,user.last_name, user.username,user.email ) is not None :
            user.save()
            messages.error(request, 'Your information has been updated successfully.')
            return redirect('profile')
        else:
            user = request.user
        return render(request, 'changeinfo.html', {'user': user}) 

    else:
        user = request.user
        return render(request, 'changeinfo.html', {'user': user}) 
    
#passwordresetfunction     
def passwordreset(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            messages.success(request, 'Password reset email has been sent.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'No user with that email found.')
            return redirect('passwordreset')
    return render(request, 'passwordreset.html')

#userprofilefunction 
def profile(request):
    user = request.user
    return render(request, 'profile.html', { 'user': user})

#logoutfunction
def userlogout(request):
    logout(request)
    return redirect('/')
