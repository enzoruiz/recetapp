# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recetas', '0002_auto_20160310_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuntuacionRecetaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('puntuacion', models.CharField(max_length=1)),
                ('receta', models.ForeignKey(to='recetas.Receta')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
