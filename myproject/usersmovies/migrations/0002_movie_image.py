# Generated by Django 5.1.4 on 2025-01-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersmovies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movies/'),
        ),
    ]
