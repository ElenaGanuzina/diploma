# Generated by Django 5.0 on 2023-12-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0002_remove_comment_image_remove_comment_modify_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
