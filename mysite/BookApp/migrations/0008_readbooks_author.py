# Generated by Django 4.2.1 on 2023-05-13 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0007_author_delete_year_remove_readbooks_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='readbooks',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='BookApp.author', verbose_name='Автор'),
        ),
    ]
