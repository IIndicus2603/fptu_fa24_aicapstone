# Generated by Django 5.0.6 on 2024-11-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_tag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.TextField(blank=True, default=''),
        ),
    ]
