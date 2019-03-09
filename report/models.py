from django.db import models
import uuid

# Create your models here.
class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car_plate = models.CharField(verbose_name='Placa', max_length=6)
    type = models.TextField(verbose_name='Tipo')
    score = models.CharField(verbose='Calificación')
    comment = models.TextField(verbose_name='Comentario')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)