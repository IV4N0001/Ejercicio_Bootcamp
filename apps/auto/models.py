from django.db import models
from apps.user.models import User
from apps.brand.models import Brand

class Auto(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name='ID Marca', primary_key=True)
    placa = models.CharField(max_length=20, verbose_name='Placa')
    km = models.PositiveSmallIntegerField(verbose_name='Kilometraje', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return self.placa
