# images/models.py
from django.db import models
import os
from PIL import Image as PILImage

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or 'No description'

    def save(self, *args, **kwargs):
        # Resize main image and generate thumbnail
        if self.image:
            img = PILImage.open(self.image)
            img = img.resize((800, 600))  # Resize main image
            img.save(self.image.path)

            # Create thumbnail
            thumbnail_img = img.copy()
            thumbnail_img = thumbnail_img.resize((150, 150))  # Resize thumbnail
            thumbnail_path = os.path.join('media', 'thumbnails', os.path.basename(self.image.name))
            thumbnail_img.save(thumbnail_path)
            self.thumbnail = 'thumbnails/' + os.path.basename(self.image.name)

        super().save(*args, **kwargs)
