# Generated by Django 5.0.6 on 2024-11-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_remove_image_thumbnail_image_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
    ]
