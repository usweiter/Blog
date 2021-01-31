from django import forms
from .models import ModelImage
from urllib import request
from django.core.files.base import ContentFile

class FormAddImage(forms.ModelForm):
    class Meta:
        model = ModelImage
        fields = ('url', )
        widgets = {
            'url': forms.HiddenInput
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        
        if extension not in valid_extensions:
            raise forms.ValidationError('Wrong extension')

        return url

    def save(self, force_insert=False, commit=True):
        model_image = super(ModelImage, self).save(commit=False)
        url_image = self.cleaned_data['url']
        name_image = model_image.id
        response = request.urlopen(url_image)
        model_image.image.save(name_image, ContentFile(response.read()), save=False)
        
        if commit:
            model_image.save()
            
        else:
            return model_image