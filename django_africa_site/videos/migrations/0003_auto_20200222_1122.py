# Generated by Django 3.0.3 on 2020-02-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20200222_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='videocategory',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
