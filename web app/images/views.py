# images/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from .forms import ImageForm

def image_upload(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Return JSON response with the URL of the uploaded image
            return JsonResponse({'image_url': image_instance.image.url})
    else:
        form = ImageForm()

    images = Image.objects.all()  # Fetch all images for display
    return render(request, 'images/image_slider.html', {'form': form, 'images': images})

def image_slider(request):
    # Fetch images from the database or other source
    images = Image.objects.all()  # Example, adjust according to your model
    return render(request, 'image_slider.html', {'images': images})

from django.http import JsonResponse

def image_check_duplicate(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        
        # Check if file already exists in the database
        exists = Image.objects.filter(image__icontains=file_name).exists()
        
        return JsonResponse({'exists': exists})
