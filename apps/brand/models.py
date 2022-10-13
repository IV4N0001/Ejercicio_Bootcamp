from django.db import models

class Brand(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name='ID Marca', primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name