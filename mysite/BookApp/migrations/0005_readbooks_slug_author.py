# Generated by Django 4.2.1 on 2023-05-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0004_remove_readbooks_year_of_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='readbooks',
            name='slug_author',
            field=models.SlugField(blank=True, verbose_name='Url автора'),
        ),
    ]
