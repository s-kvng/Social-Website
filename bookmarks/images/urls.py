from django.urls import path
from . import views

#Create image urls

app_name = 'images' #research

urlpatterns = [
    path('create/', views.image_create, name='create'),
]
