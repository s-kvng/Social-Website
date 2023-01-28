from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST


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



def image_detail(request, id , slug):
    imageObj = get_object_or_404(Image, id=id, slug=slug)

    return render(request, 'images/image/details.html' , {'imageObj': imageObj})



@login_required
@require_POST
def image_like(request):

    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            imageObj = Image.objects.get(id=image_id)

            if action == 'like':
                imageObj.users_like.add(request.user)
            else:
                imageObj.users_like.remove(request.user)

            return JsonResponse({'status': 'ok'})
        except Image.DoesNotExist:
            pass

    return JsonResponse({'status': 'error'})




