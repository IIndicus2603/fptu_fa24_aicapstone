# Generated by Django 5.0.6 on 2024-11-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.TextField(blank=True, default=''),
        ),
    ]
