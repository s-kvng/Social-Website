from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm , UserRegistrationForm , UserEditForm , ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def user_login(request): # Our own custom view
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            
            #check the datebase for an object with the same username and password
            user = authenticate(request, username=cd['username'],password=cd['password'])
            
            #when a user object is found
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authentication successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid logins')   
    else:
        form = LoginForm()
    
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


#custom registeration view 
def register(request):
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            #create a new user but avoid saving it yet
            new_user = user_form.save(commit=False)
            print(new_user)
            
            #set the chosen password... set_password hashes the password so we dont store the raw one 
            new_user.set_password(user_form.cleaned_data['password'])
            
            #save the User object
            new_user.save()
            
            #create user profile
            Profile.objects.create(user = new_user)
            
            return render(request, 'account/register_done.html', {'new_user': new_user})
            
            
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request):
    
    if request.method == 'POST':
        
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)
        
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
