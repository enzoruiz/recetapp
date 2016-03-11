# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_receta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, blank=True, upload_to='img-receta'),
        ),
    ]
