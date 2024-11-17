# images/views.py
import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse
import logging

def image_upload(request):
    if request.method == 'POST' and request.FILES.get('image'):
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()

            # Get the file name (only the file name, not the full path)
            file_name = os.path.basename(image_instance.image.name)

            # Load the tag.json file
            tag_file_path = os.path.join(settings.BASE_DIR, 'tag.json')
            if os.path.exists(tag_file_path):
                with open(tag_file_path, 'r') as f:
                    tag_data = json.load(f)

                # Extract tags based on the file name
                tags = tag_data.get(file_name, [])

                # Assign tags to the image and save
                image_instance.tags = tags
                image_instance.save()

            # Return JSON response with the URL of the uploaded image and tags
            return JsonResponse({'image_url': image_instance.image.url, 'tags': image_instance.tags})
    else:
        form = ImageForm()

    images = Image.objects.all()  # Fetch all images for display
    return render(request, 'images/image_slider.html', {'form': form, 'images': images})
    
def image_slider(request):
    # Fetch images and their associated tags from the database
    images = Image.objects.all()  # Adjust according to your model
    return render(request, 'image_slider.html', {'images': images})

def image_check_duplicate(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        
        # Check if file already exists in the database
        exists = Image.objects.filter(image__icontains=file_name).exists()
        
        return JsonResponse({'exists': exists})


