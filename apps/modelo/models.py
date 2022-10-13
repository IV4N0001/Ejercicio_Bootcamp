from django.db import models
from apps.brand.models import Brand

class Modelo(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name='ID Modelo', primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Nombre')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name

