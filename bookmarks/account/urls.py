from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #prevous login url defined
    #path('login/', views.user_login, name='login')
    
    #built-in django authentication views
    #Login / logout urls
    #path('login/', auth_views.LoginView.as_view(), name='login'), 
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    
    #change password urls

    #path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    
    #reset password urls
    #path('password-reset/' , auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('password-reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #django default url patterns for the authentication views
    path('', include('django.contrib.auth.urls')),
    
    
    #dashboard url
    path('', views.dashboard, name='dashboard'),
    
    #register url
    path('register/', views.register, name='register'),
    
]
