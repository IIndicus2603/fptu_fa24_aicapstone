# Generated by Django 5.0.6 on 2024-11-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]