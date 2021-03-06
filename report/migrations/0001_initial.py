# Generated by Django 2.1.7 on 2019-03-09 20:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('car_plate', models.CharField(max_length=6, verbose_name='Placa')),
                ('type', models.CharField(max_length=20, verbose_name='Tipo')),
                ('score', models.CharField(max_length=1, verbose_name='Calificación')),
                ('comment', models.TextField(verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
