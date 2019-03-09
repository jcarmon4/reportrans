from django.db import models
import uuid

# Create your models here.
class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_plate = models.CharField(verbose_name='Placa', max_length=6)
    type = models.CharField(verbose_name='Tipo', max_legth=20)
    score = models.CharField(verbose_name='Calificación', max_length=1)
    comment = models.TextField(verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)