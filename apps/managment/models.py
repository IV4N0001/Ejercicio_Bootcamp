from django.db import models
from apps.auto.models import Auto

class Managment(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name='ID Auto', primary_key=True)
    km = models.PositiveSmallIntegerField(verbose_name='Kilometraje', default=0)
    direccion = models.CharField(max_length=1000, verbose_name='Dirección')
    costo = models.IntegerField(verbose_name='Costo', default=0)
    fecha = models.DateField(verbose_name='Fecha de mantenimiento')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    parseo = str(id)
    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return self.id