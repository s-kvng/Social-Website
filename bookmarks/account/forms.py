from django import forms 
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
class UserRegistrationForm(forms.ModelForm):
     
    password = forms.CharField(label='Password',widget = forms.PasswordInput(attrs={'class': 'form-control mb-1'}))
    password2 = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class': 'form-control mb-1'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name','email']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control mb-1'}),
            'email' : forms.TextInput(attrs={'class': 'form-control mb-1'}),
               
        }
      
     #specific clean validation function to handle password  validation   
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise forms.ValidationError('Email already exists')
        return data
      


class UserEditForm(forms.ModelForm): # form to edit user information
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
        }
      
     #validation to check if email already exists   
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id = self.instance.id).filter(email = data)
        
        if qs.exists():
            raise forms.ValidationError('Email is already in use')
        return data
        
    
class ProfileEditForm(forms.ModelForm): #form to edit profile information
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2000-01-01'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }

            
