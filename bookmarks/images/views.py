from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm 

# Create your views here.

@login_required
def image_create(request):
    
    if request.method == 'POST':
        
        form = ImageCreateForm(data=request.POST)
        
        if form.is_valid():
            #get item obj but not save to database
            new_image = form.save(commit=False)
            
            #assign current user to the item(image)
            new_image.user = request.user
            new_image.save()
            

            messages.success(request,'Image added successfully')
            
            #redirect to newly created item detail_view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(request.GET)
        
        return render(request, 'images/image/create.html', {'section': 'images', 'form': form})