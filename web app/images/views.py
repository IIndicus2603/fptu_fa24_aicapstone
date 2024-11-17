# images/views.py
import json
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Image
from .forms import ImageForm
from django.http import JsonResponse

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

def update_tag(request):
    if request.method == 'POST':
        tag_file_path = os.path.join(settings.BASE_DIR, 'tag.json')

        image_path = request.POST.get('image_name')  # Image name
        old_tag = request.POST.get('old_tag')        # Old tag
        new_tag = request.POST.get('new_tag')        # New tag
        image_name = os.path.basename(image_path)
        if not (image_name and old_tag and new_tag):
            return JsonResponse({'success': False, 'error': 'Missing data'}, status=400)

        # Read the tag.json file
        try:
            with open(tag_file_path, 'r', encoding='utf-8') as file:
                tags = json.load(file)
        except FileNotFoundError:
            return JsonResponse({'success': False, 'error': 'tag.json file not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON in tag.json'}, status=500)

        # Check if the image exists in the tag data
        if image_name not in tags:
            return JsonResponse({'success': False, 'error': 'No tags found for this image in tag.json'}, status=400)

        # Check if old_tag exists in the image's tags
        if old_tag in tags[image_name]:
            tags[image_name] = [new_tag if tag == old_tag else tag for tag in tags[image_name]]

            # Save the updated tags to tag.json
            try:
                with open(tag_file_path, 'w', encoding='utf-8') as file:
                    json.dump(tags, file, ensure_ascii=False, indent=4)
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)}, status=500)

            return JsonResponse({'success': True, 'tags': tags[image_name]})
        else:
            return JsonResponse({'success': False, 'error': 'Old tag not found'}, status=400)

    return JsonResponse({'success': False}, status=400)

