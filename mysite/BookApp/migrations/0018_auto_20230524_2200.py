# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def make_many_categories(apps, schema_editor):
    ReadBooks = apps.get_model('категории', 'ReadBooks')

    for book in ReadBooks.objects.all():
        book.categories.add(book.category)


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0017_alter_category_options_readbooks_categories'),
    ]

    operations = [
        migrations.RunPython(make_many_categories),
    ]
