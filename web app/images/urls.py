# images/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_slider, name='image_slider'),  # Ensure 'image_slider' is the correct name
    path('images/upload/', views.image_upload, name='image_upload'),
    path('images/check_duplicate/', views.image_check_duplicate, name='image_check_duplicate'),

]
