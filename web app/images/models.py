from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255, blank=True)
    tags = models.TextField(blank=True, default="")  # Add this line to store tags

    def __str__(self):
        return self.description or 'No description'