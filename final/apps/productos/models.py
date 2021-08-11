from django.db import models

from apps.core.models import TimeModel

from apps.genericos.models import SubRubro

class Producto(TimeModel):
	nombre = models.CharField(max_length = 30)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	stock = models.IntegerField(default = 0)
	subrubro = models.ForeignKey(SubRubro, on_delete = models.SET_NULL , null = True)

