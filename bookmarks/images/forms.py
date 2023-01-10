from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests

#Create a new form

class ImageCreateForm(forms.ModelForm):
    class Meta :
        model = Image 
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
            'title': forms.TextInput(attrs={'class': 'form-control' ,'id' : 'sp-form'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        
    def clean_url(self):
        url = self.cleaned_data['url'] # url is retrieved from the cleaned_data dictionary of the form
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.',1)[1].lower()
        
        if extension not in valid_extensions:
            raise forms.ValidationError('The given url does not match any valid image extensions')
        return url
    
    
    #Overriding the save method
    def save(self, force_insert=False, force_update=False, commit = True):
        
        image = super().save(commit=False) # Save the image instance 
        image_url = self.cleaned_data['url']
        name = slugify(image.title) #
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}' # combine the slug name and extension
        
        #download image from the given url
        reponse = requests.get(image_url) # store the response in the response object after the http GET request has been sent

        # file is saved to the media dictectory of your project
        #using the save method of the image field
        image.image.save(image_name, ContentFile(reponse.content), save=False)
        if commit:
            image.save()
        return image
        