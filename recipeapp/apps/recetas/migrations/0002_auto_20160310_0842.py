# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='titulo',
            field=models.CharField(max_length=45, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receta',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
