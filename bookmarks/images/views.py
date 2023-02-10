from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.http import HttpResponse


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


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)

    #retrieving data from get
    page = request.GET.get('page')
    images_only = request.GET.get('images_only')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)

    except EmptyPage:
        if images_only:

            return HttpResponse('')

        images = paginator.page(paginator.num_pages)

    if images_only:
        return render(request, 'images/image/list_images.html', {'section': 'images', 'images': images})

    return render(request, 'images/image/list.html', {'section': 'images', 'images': images})







