# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0003_puntuacionrecetauser'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, blank=True, upload_to='img-receta/'),
        ),
    ]
