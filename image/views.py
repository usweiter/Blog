from django.shortcuts import render
from .models import ModelImage
from .forms import FormAddImage

def add_image(request):
    
    return render(request, 'image/add_image.html', {})